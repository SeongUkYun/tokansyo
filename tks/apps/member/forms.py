# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from models import member as Member


class MemberForm(forms.ModelForm):
    address = forms.CharField(widget=forms.TextInput(attrs={'size': 50}))

    class Meta:
        model = Member
        fields = ['accessibility', 'rank', 'name', 'popular_name',
                  'job_title', 'company_name', 'biz_type', 'tel', 'fax',
                  'zipcode', 'address']
