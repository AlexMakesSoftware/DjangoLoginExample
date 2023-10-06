from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView


class ProfileView(TemplateView):
    template_name = 'customise_login/profile.html'
