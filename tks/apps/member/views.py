from django import forms
from django.views import generic
from django.shortcuts import render
from django.views.generic import TemplateView
from django.db.models import Q
from models import member as Member
from forms import MemberForm


class MemberMixin(object):
    def get_queryset(self):
        return Member.objects.filter(~Q(accessibility=3))


class MemberListView(MemberMixin, generic.ListView):
    paginate_by = 10
    template_name = 'member/member_list.html'

    def get_context_data(self, **kwargs):
        context = super(MemberListView, self).get_context_data(**kwargs)
        if self.request.user.is_active:
            context['members'] = self.get_queryset()
        else:
            context['members'] = self.get_queryset().filter(accessibility=1)

        return context


class MemberView(generic.DetailView):
    model = Member
    template_name = 'member/member_detail.html'

    def get_context_data(self, **kwargs):
        context = super(MemberView, self).get_context_data(**kwargs)

        return context


class MemberEditView(TemplateView):
    template_name = 'member/edit.html'

    def get_context_data(self, **kwargs):
        context = super(MemberEditView, self).get_context_data(**kwargs)
        member = Member.objects.get(auth_user=self.request.user)
        context['member'] = member
        context['form'] = MemberForm(instance=member)

        return context


class MemberCompleteView(TemplateView):
    template_name = 'member/complete.html'

    def get_context_data(self, **kwargs):
        context = super(MemberCompleteView, self).get_context_data(**kwargs)

        member = Member.objects.get(auth_user=self.request.user)
        member.accessibility = self.request.GET['accessibility']
        member.rank = self.request.GET['rank']
        member.name = self.request.GET['name']
        member.popular_name = self.request.GET['popular_name']
        member.job_title = self.request.GET['job_title']
        member.company_name = self.request.GET['company_name']
        member.biz_type = self.request.GET['biz_type']
        member.tel = self.request.GET['tel']
        member.fax = self.request.GET['fax']
        member.zipcode = self.request.GET['zipcode']
        member.address = self.request.GET['address']
        member.save()

        return context
