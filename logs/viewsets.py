from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter

from logs.models import LogEntry
from logs.serializers import LogEntrySerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_query_param = 'page'
    max_page_size = 1000

class LogEntryViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [SearchFilter,]
    search_fields = ['ip_address', 'method', 'uri', 'response_code']
