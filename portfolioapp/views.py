# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import User
import pdb


def main_data_view(request):

    return render(request, 'portfolioapp/main.html', {'data': __getuserdata()})


def about_view(request):

    # pdb.set_trace()
    return render(request, 'portfolioapp/about.html', {'data': __getuserdata()})


def contact_view(request):

    # pdb.set_trace()
    return render(request, 'portfolioapp/contact.html', {'data': __getuserdata()})


def __getuserdata():
    data = User.objects.select_related().filter(username='Javier')
    return data
