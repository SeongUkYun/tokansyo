from django.views import generic
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import news as News


class TokanNewsMixin(object):
    def get_queryset(self):
        return News.objects.filter(news_type='N').order_by('-created_at')


class TokanNewsListView(TokanNewsMixin, generic.ListView):
    paginate_by = 10
    template_name = 'news/tokan_list.html'

    def get_context_data(self, **kwargs):
        context = super(TokanNewsListView, self).get_context_data(**kwargs)
        context['newses'] = self.get_queryset()

        return context


class TokanNewsView(generic.DetailView):
    model = News
    template_name = 'news/tokan_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TokanNewsView, self).get_context_data(**kwargs)

        return context


class TaxNewsMixin(object):
    def get_queryset(self):
        return News.objects.filter(news_type='T').order_by('-created_at')


class TaxNewsListView(TaxNewsMixin, generic.ListView):
    paginate_by = 10
    template_name = 'news/tax_list.html'

    def get_context_data(self, **kwargs):
        context = super(TaxNewsListView, self).get_context_data(**kwargs)
        context['newses'] = self.get_queryset()

        return context


class TaxNewsView(LoginRequiredMixin, generic.DetailView):
    model = News
    template_name = 'news/tax_detail.html'

    def get_context_data(self, **kwargs):
        context = super(TaxNewsView, self).get_context_data(**kwargs)

        return context


class WeekNewsMixin(object):
    def get_queryset(self):
        return News.objects.filter(news_type='W').order_by('-created_at')


class WeekNewsListView(WeekNewsMixin, generic.ListView):
    paginate_by = 10
    template_name = 'news/week_list.html'

    def get_context_data(self, **kwargs):
        context = super(WeekNewsListView, self).get_context_data(**kwargs)
        context['newses'] = self.get_queryset()

        return context


class WeekNewsView(LoginRequiredMixin, generic.DetailView):
    model = News
    template_name = 'news/week_detail.html'

    def get_context_data(self, **kwargs):
        context = super(WeekNewsView, self).get_context_data(**kwargs)

        return context
