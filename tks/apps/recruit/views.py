from django.views import generic
from django.shortcuts import render
from .models import recruit as Recruit


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
