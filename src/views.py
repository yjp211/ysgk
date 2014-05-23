# -*- coding:utf-8 -*-
from django.shortcuts import render

def home(request, template='index.html'):
    """
    home index for src
    """
    return render(request, template)
