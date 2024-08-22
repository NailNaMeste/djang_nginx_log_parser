from django.db import models

class LogEntry(models.Model):
    ip_address = models.CharField(max_length=255)
    date = models.DateTimeField()
    method = models.CharField(max_length=10)
    uri = models.CharField(max_length=255)
    response_code = models.IntegerField()
    response_size = models.IntegerField(null=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.method} {self.uri} {self.response_code}'
