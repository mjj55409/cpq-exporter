from django.conf import settings
from django.db import models
from model_utils.models import TimeStampedModel
# from django.template.defaultfilters import slugify
from django.utils.translation import ugettext_lazy as _


class Repository (models.Model):
    name = models.CharField(max_length=100, unique=True)
    url = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.name


class KB (models.Model):
    name = models.CharField(max_length=30, unique=True)
    repository = models.ForeignKey(Repository)

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
    type = models.SmallIntegerField(choices=TYPE_CHOICES, default=0)
    client = models.CharField(max_length=3, default='000', blank=False)


class DatabaseDestination (models.Model):
    TYPE_MSSQL = 0
    TYPE_MYSQL = 1
    TYPE_JDBC = 2

    TYPE_CHOICES = (
        (TYPE_MSSQL, _('Microsoft SQL')),
        (TYPE_MYSQL, _('MYSQL')),
        (TYPE_JDBC, _('Java Connector'))
    )

    destination = models.OneToOneField(Destination, primary_key=True)
    database_type = models.SmallIntegerField(choices=TYPE_CHOICES, default=0)
    host = models.CharField(max_length=100, blank=True)
    port = models.CharField(max_length=7, blank=True)
    database_name = models.CharField(max_length=100, blank=False)


class SAPDestination (models.Model):
    destination = models.OneToOneField(Destination, primary_key=True)
    host = models.CharField(max_length=100, blank=False)
    sid = models.CharField(max_length=4, blank=False)


class Export (TimeStampedModel):
    name = models.CharField(max_length=80, unique=True, blank=False)
    destination = models.ForeignKey(Destination)
    kb = models.ManyToManyField(KB)
