from django.views import generic
from django.shortcuts import render
from django.db.models import Q
from .models import member as Member


class MemberMixin(object):
    def get_queryset(self):
        return Member.objects.filter(~Q(accessibility=3))


class MemberListView(MemberMixin, generic.ListView):
    paginate_by = 10
    template_name = 'member/member_list.html'

    def get_context_data(self, **kwargs):
        context = super(MemberListView, self).get_context_data(**kwargs)
        context['members'] = self.get_queryset()

        return context


class MemberView(generic.DetailView):
    model = Member
    template_name = 'member/member_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MemberView, self).get_context_data(**kwargs)

        return context
