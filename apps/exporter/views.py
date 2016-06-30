from django.views.generic import ListView, DetailView
from exporter import models


class ExportList (ListView):
    #model = models.Execution
    context_object_name = "export_jobs"
    queryset = models.Execution.objects.all()
    template_name='exporter/jobs/index.html'


class ProjectDetail (DetailView):
    model = models.Project
    template_name='exporter/jobs/detail.html'
