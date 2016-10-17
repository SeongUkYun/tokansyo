# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from models import inquiry as Inquiry


class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['email', 'title', 'content']
