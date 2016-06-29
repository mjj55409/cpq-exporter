# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(LoginRequiredMixin, TemplateView):
    login_url = 'accounts/login/'
    redirect_field_name = 'home'
    template_name = 'pages/home.html'
