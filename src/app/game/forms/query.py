# -*- coding:utf-8 -*-

from django import forms

class GameQueryForm(forms.Form):

    key_word = forms.CharField(required=False)
    tags = forms.CharField(required=False)
    categorys = forms.CharField(required=False)

    sort_field = forms.CharField(required=False)
    sort_type = forms.CharField(required=False)

