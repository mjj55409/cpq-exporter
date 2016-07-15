from django.conf import settings
from django.db import models
# from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class KB (models.Model):
    name = models.CharField(max_length=30, unique=True)
    repository_url = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class Destination (models.Model):
    TYPE_DB = 0
    TYPE_ECC = 1
    TYPE_CRM = 2

    TYPE_CHOICES = (
        (TYPE_DB, _('Database')),
        (TYPE_ECC, _('ECC System')),
        (TYPE_CRM, _('CRM System'))
    )

    name = models.CharField(max_length=30)
    destination_type = models.SmallIntegerField(choices=TYPE_CHOICES, default=0)
    client = models.CharField(max_length=3, default='000', blank=False)

    def __str__(self):
        return self.name


class DatabaseDestination (models.Model):
    TYPE_MSSQL = 0
    TYPE_MYSQL = 1
    TYPE_JDBC = 2

    TYPE_CHOICES = (
        (TYPE_MSSQL, _('Microsoft SQL')),
        (TYPE_MYSQL, _('MYSQL')),
        (TYPE_JDBC, _('Java Connector'))
    )

    destination = models.OneToOneField(Destination, on_delete=models.CASCADE, primary_key=True)
    database_type = models.SmallIntegerField(choices=TYPE_CHOICES, default=0)
    host = models.CharField(max_length=100, blank=True)
    port = models.CharField(max_length=7, blank=True)
    database_name = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.database_name + '@' + self.host + ':' + self.port


class SAPDestination (models.Model):
    destination = models.OneToOneField(Destination, on_delete=models.CASCADE, primary_key=True)
    host = models.CharField(max_length=100, blank=False)
    sid = models.CharField(max_length=4, blank=False)


class Project (models.Model):
    name = models.CharField(max_length=40, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class ProjectStep (models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='steps')
    step_number = models.PositiveSmallIntegerField(null=False, default=1)
    name = models.CharField(max_length=40, blank=True)
    kb = models.ForeignKey(KB)

    def __str__(self):
        return self.project.name + '.' + self.kb.name


class Execution (models.Model):
    project = models.ForeignKey(Project)
    time_start = models.DateTimeField(null=True, blank=True)
    time_end = models.DateTimeField(null=True, blank=True)
    duration = models.DurationField(blank=True, null=True)
    export_status = models.BooleanField(blank=True)


class ExecutionStep (models.Model):
    execution = models.ForeignKey(Execution)
    step = models.ForeignKey(ProjectStep)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    status = models.BooleanField()
