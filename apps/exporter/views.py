from django.views.generic import ListView, DetailView
from exporter import models


class ProjectList (ListView):
    model = models.Project
    template_name='exporter/jobs/index.html'


class ProjectDetail (DetailView):
    model = models.Project
    template_name='exporter/jobs/detail.html'
