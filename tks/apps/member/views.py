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
        return Member.objects.filter(~Q(accessibility=3)).order_by('rank', 'name').exclude(company_name__isnull=True).exclude(company_name__exact='')


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
        context['reset_form'] = PasswordResetForm()

        return context


class MemberCompleteView(TemplateView):
    template_name = 'member/complete.html'

    def post(self, request, *args, **kwargs):
        id = int(request.POST['member_id'])
        member = Member.objects.get(pk=id)
        form = MemberForm(request.POST, request.FILES, instance=member)
        form.save()
        return render(request, self.template_name)


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
        name = self.request.GET['password']

        context['message'] = '申込受付を完了しました。'

        content = '{0}様からログイン設定申請が届きました。\n連絡先電話番号は{1}です。'.format(name, tel)
        message = EmailMessage(
            'ログイン設定申請が届きました。',
            content,
            'tks@tokansho.org',
            ['tks@tokansho.org'],
            ['tokansho@gmail.com'],
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
