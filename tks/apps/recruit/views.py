# coding: utf-8
from __future__ import unicode_literals

from django.views import generic
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from models import recruit as Recruit
from forms import RecruitForm


class RecruitMixin(object):
    def get_queryset(self):
        return Recruit.objects.all()


class RecruitListView(RecruitMixin, generic.ListView):
    paginate_by = 10
    template_name = 'recruit/list.html'

    def get_context_data(self, **kwargs):
        context = super(RecruitListView, self).get_context_data(*kwargs)
        context['recruits'] = self.get_queryset().filter(status='P')

        return context


class RecruitView(generic.DetailView):
    model = Recruit
    template_name = 'recruit/detail.html'

    def get_context_data(self, **kwargs):
        context = super(RecruitView, self).get_context_data(**kwargs)

        return context


class RecruitApplyView(TemplateView):
    template_name = 'recruit/apply.html'

    def get_context_data(self, **kwargs):
        context = super(RecruitApplyView, self).get_context_data(**kwargs)
        context['form'] = RecruitForm()

        return context


class RecruitApplyCompleteView(TemplateView):
    template_name = 'recruit/complete.html'

    def post(self, request, *args, **kwargs):
        form = RecruitForm(request.POST, request.FILES)
        form.save()

        return render(request, self.template_name)
