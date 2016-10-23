from django import forms
from django.views import generic
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
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

        message = EmailMessage(
            self.request.GET['title'],
            self.request.GET['content'],
            self.request.GET['email'],
            ["tks@tokansho.org"],
            ["dordory@gmail.com"],
            headers={'Reply-To': 'tks@tokansho.org'})
        message.send()

        return context
