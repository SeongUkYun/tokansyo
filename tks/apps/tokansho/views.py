from django.shortcuts import render
from django.views import generic

from ..calendar.models import task as CalendarTask
from ..recruit.models import recruit as Recruit
from ..news.models import news as News


class HomeView(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        tasks = CalendarTask.objects.all().order_by('-id')[:2]
        context['tasks'] = tasks
        recruits = Recruit.objects.all().order_by('-id')[:2]
        context['recruits'] = recruits
        TokanNews = News.objects.filter(news_type='N').order_by('-id')[:2]
        context['tokanNews'] = TokanNews
        TaxNews = News.objects.filter(news_type='T').order_by('-id')[:2]
        context['taxNews'] = TaxNews
        WeekNews = News.objects.filter(news_type='W').order_by('-id')[:2]
        context['weekNews'] = WeekNews
        return context
