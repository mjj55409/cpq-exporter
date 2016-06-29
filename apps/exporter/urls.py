# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from exporter.views import ProjectDetail


urlpatterns = [
    url(r'^project/(?P<pk>[0-9]+)/$', ProjectDetail.as_view(), name='project-detail')
]
