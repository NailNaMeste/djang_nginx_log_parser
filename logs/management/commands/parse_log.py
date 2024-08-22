import datetime
import json
import multiprocessing
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

from django.core.management import BaseCommand
from django.conf import settings
from logs.models import LogEntry


class Command(BaseCommand):
    help = 'Parse and insert log entries into the database.'

    def add_arguments(self, parser):
        parser.add_argument('log_file', type=str, help='Path to the log file')

    def process_log_lines(self, lines):
        with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count()) as executor:
            results = []
            for entry in executor.map(self.parse_log_entry, lines):
                results.append(entry)
                if len(results) == settings.DB_CHUNK_SIZE:
                    self.save_log_entries(results)
        self.save_log_entries(results)

    def parse_log_entry(self, line):
        data = json.loads(line)
        entry = LogEntry(
            ip_address=data['remote_ip'],
            date=datetime.datetime.strptime(data['time'], '%d/%b/%Y:%H:%M:%S %z'),
            method=data['request'].split()[0],
            uri=data['request'].split('/', 3)[-1].split(' ', 1)[0],
            response_code=int(data['response']),
            response_size=int(data.get('bytes', None))
        )
        return entry

    def save_log_entries(self, r):
        LogEntry.objects.bulk_create(r)
        r.clear()
        self.stdout.write(f'Chunk saved')

    def handle(self, *args, **options):
        with open(options['log_file'], 'r') as log_file:
            lines = log_file.readlines()
        self.process_log_lines(lines)
        self.stdout.write(f'Parsed and saved log entries from {options["log_file"]}.')