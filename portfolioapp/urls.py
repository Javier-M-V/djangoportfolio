# -*- coding: utf-8 -*-
from django.urls import path
from portfolioapp.views import main_data_view,about_view , contact_view


urlpatterns = [
    path('', main_data_view, name='main'),
    path('about', about_view, name='about'),
    path('contact', contact_view, name='contact'),
]