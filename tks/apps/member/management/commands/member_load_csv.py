# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django.db import transaction
from backports import csv
import io
import os

from ...models import member as Member


class Command(BaseCommand):
    help = "Load member data from csv file."

    def add_arguments(self, parser):
        parser.add_argument("-f", "--filename", help="source file name")

    @transaction.atomic
    def handle(self, *args, **options):

        def create_mail(str):
            seed = str.replace('-', '')
            return '{0}@tokansho.org'.format(seed)

        print os.path.basename(options['filename'])
        os.chdir(os.path.dirname(options['filename']))
        filename = os.path.basename(options['filename'])

        reader = csv.reader(io.open(filename, encoding="utf-8"),delimiter=',')
        reader.next()
        for i, row in enumerate(reader):
            if not row[11]:
                continue
            user = User.objects.create_user(row[11].replace('-', ''),
                                            create_mail(row[11]),
                                            row[11].replace('-', ''))

            # print '{0}-{1}'.format(row[2], row[3])
            # print '{0}-{1}-{2}-{3}'.format(row[1], row[4], row[5], row[6])
            # print '{0}-{1}-{2}-{3}'.format(row[7], row[8], row[9], row[10])

            if row[0] == '公開':
                accessibility = 1
            elif row[0] == '会員':
                accessibility = 2
            else:
                accessibility = 3

            if row[1] == '名誉会長':
                rank = '00'
            elif row[1] == '会長':
                rank = '01'
            elif row[1] == '部会長':
                rank = '02'
            elif row[1] == '常任理事':
                rank = '03'
            elif row[1] == '監事':
                rank = '04'

            member, c = Member.objects.update_or_create(
                auth_user = user,
                name = row[2],
                popular_name = row[3],
                defaults = {
                    'accessibility': accessibility,
                    'rank': rank,
                    'job_title': row[4],
                    'company_name': row[5],
                    'biz_type': row[6],
                    'tel': row[7],
                    'fax': row[8],
                    'zipcode': row[9].strip(),
                    'address': row[10],
                    })

            _first_name =  member.first_name()
            _last_name = member.last_name()
            if _first_name:
                user.first_name = member.first_name()
            if _last_name:
                user.last_name = member.last_name()
            user.save()
