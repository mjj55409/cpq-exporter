from django.views.generic import ListView
from exporter.models import Export


class JobList (ListView):
    model = Export
