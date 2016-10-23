# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from models import member as Member


class MemberForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    popular_name = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    job_title = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    company_name = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    biz_type = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    tel = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    fax = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    zipcode = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))
    address = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))

    class Meta:
        model = Member
        fields = ['accessibility', 'rank', 'name', 'popular_name',
                  'job_title', 'company_name', 'biz_type', 'tel', 'fax',
                  'zipcode', 'address']


class ApplyPasswordForm(forms.Form):
    tel = forms.CharField(label='tel number', max_length=20)
    password = forms.CharField(label='password', max_length=32)


class PasswordResetForm(forms.Form):
    password = forms.CharField(widget=forms.TextInput(attrs={'size': 50}), label='password', max_length=32)
