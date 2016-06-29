from django.views.generic import ListView
from exporter import models


class ProjectList (ListView):
    model = models.Project
