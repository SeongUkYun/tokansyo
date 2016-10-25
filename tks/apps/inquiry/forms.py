# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from models import inquiry as Inquiry


class InquiryForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'size': 42}))
    title = forms.CharField(widget=forms.TextInput(attrs={'size': 42}))
    content = forms.Field(widget=forms.Textarea(attrs={'style': 'width: 42;'}))

    class Meta:
        model = Inquiry
        fields = ['email', 'title', 'content']
