from django import forms
from django.views import generic
from django.shortcuts import render
from django.views.generic import TemplateView
from models import inquiry as Inquiry
from forms import InquiryForm


class InquiryMixin(object):
    def get_queryset(self):
        return Inquiry.objects.all()

class InquiryView(TemplateView):
    template_name = 'inquiry/inquiry.html'

    def get_context_data(self, **kwargs):
        context = super(InquiryView, self).get_context_data(**kwargs)
        inquiry = Inquiry()
        context['form'] = InquiryForm(instance=inquiry)

        return context


class InquiryCompleteView(TemplateView):
    template_name = "inquiry/complete.html"

    def get_context_data(self, **kwargs):
        context = super(InquiryCompleteView, self).get_context_data(**kwargs)

        inquiry = Inquiry.objects.create()
        inquiry.email = self.request.GET['email']
        inquiry.title = self.request.GET['title']
        inquiry.content = self.request.GET['content']
        inquiry.save()

        return context