# -*- coding:utf-8 -*-
from django.shortcuts import render

def home(request, template='home/index.html'):
    """
    home index for src
    """
    return render(request, template)
