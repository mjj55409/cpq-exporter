from django import forms
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from exporter import models


class ExportList (LoginRequiredMixin, ListView):
    #model = models.Execution
    context_object_name = "export_jobs"
    queryset = models.Execution.objects.all()
    template_name='exporter/jobs/index.html'


class ProjectStepForm (forms.ModelForm):
    model = models.ProjectStep
    step_number = forms.IntegerField(min_value=1, max_value=999)
    name = forms.CharField()
    kb = forms.CharField()


class ProjectDetail (LoginRequiredMixin, UpdateView):
    model = models.Project
    fields = ['name', 'description']
    template_name='exporter/jobs/detail.html'
    inline = forms.formset_factory(ProjectStepForm)
