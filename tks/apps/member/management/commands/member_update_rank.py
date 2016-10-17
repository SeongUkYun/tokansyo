# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from backports import csv
import io
import os

from ...models import member as Member


class Command(BaseCommand):
    help = "Update rank of member from csv file."

    def add_arguments(self, parser):
        parser.add_argument("-f", "--filename", help="source file name")

    @transaction.atomic
    def handle(self, *args, **options):

        print os.path.basename(options['filename'])
        os.chdir(os.path.dirname(options['filename']))
        filename = os.path.basename(options['filename'])

        reader = csv.reader(io.open(filename, encoding="utf-8"),delimiter=',')
        reader.next()
        for i, row in enumerate(reader):
            if not row[11]:
                continue

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
            else:
                rank = '05'

            member = Member.objects.get(
                name = row[2], popular_name = row[3])
            member.rank = rank
            member.save()
