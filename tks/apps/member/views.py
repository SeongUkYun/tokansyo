# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.views import generic
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.db.models import Q
from models import member as Member
from forms import MemberForm, ApplyPasswordForm, PasswordResetForm


class MemberMixin(object):
    def get_queryset(self):
        return Member.objects.filter(~Q(accessibility=3)).order_by('company_name')


class MemberListView(MemberMixin, generic.ListView):
    paginate_by = 10
    template_name = 'member/member_list.html'

    def get_context_data(self, **kwargs):
        context = super(MemberListView, self).get_context_data(**kwargs)
        if self.request.user.is_active:
            context['members'] = self.get_queryset()
        else:
            context['members'] = self.get_queryset().filter(accessibility=1).exclude(company_name__isnull=True).exclude(company_name__exact='')

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
        context['reset_form'] = PasswordResetForm()

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


class ApplyPasswordView(TemplateView):
    template_name = 'member/password.html'

    def get_context_data(self, **kwargs):
        context = super(ApplyPasswordView, self).get_context_data(**kwargs)
        context['form'] = ApplyPasswordForm()

        return context


class ApplyCompleteView(TemplateView):
    template_name = 'member/apply_complete.html'

    def get_context_data(self, **kwargs):
        context = super(ApplyCompleteView, self).get_context_data(**kwargs)

        tel = self.request.GET['tel'].replace('-', '')
        password = self.request.GET['password']
        try:
            user = User.objects.get(username=tel)
            user.set_password(password)
            user.is_active = False
            user.save()
            flag = True
        except:
            raise
            flag = False

        print flag
        content = '携帯番号{0}からパスワード設定申請が届きました。'.format(tel)
        message = EmailMessage(
            'パスワード設定申請が届きました。',
            content,
            'tks@tokansho.org',
            ['tks@tokansho.org', 'tokansho@gmail.com'],
            ['dordory@gmail.com'],
            headers={'Reply-To': 'tks@tokansho.org'})
        message.send()
        
        return context


class ResetCompleteView(TemplateView):
    template_name = 'member/complete.html'

    def get_context_data(self, **kwargs):
        context = super(ResetCompleteView, self).get_context_data(**kwargs)

        user = self.request.user
        password = self.request.GET['password']
        user.set_password(password)
        user.save()
        
        return context
