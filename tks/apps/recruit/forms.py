# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from models import recruit as Recruit


class RecruitForm(forms.ModelForm):
    company_name = forms.CharField(widget=forms.TextInput(attrs={'size': 42}))
    address = forms.CharField(widget=forms.TextInput(attrs={'size': 42}))
    tel = forms.CharField(widget=forms.TextInput(attrs={'size': 42}))
    descript = forms.CharField(widget=forms.Textarea(attrs={'style': 'width: 42;'}))
    
    class Meta:
        model = Recruit
        fields = ['company_name', 'address', 'tel', 'descript']
