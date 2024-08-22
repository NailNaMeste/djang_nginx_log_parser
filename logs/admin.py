from django.contrib import admin

from logs.models import LogEntry

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('ip_address', 'date', 'method', 'uri', 'response_code', 'response_size')
    search_fields = ('ip_address', 'uri', 'response_code')
    list_filter = ('date', 'method', 'response_code')