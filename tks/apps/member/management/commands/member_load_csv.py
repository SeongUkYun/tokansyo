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
    help = "Load member data from csv file."

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
            print '{0}-{1}'.format(row[2], row[3])
            print '{0}-{1}-{2}-{3}'.format(row[1], row[4], row[5], row[6])
            print '{0}-{1}-{2}-{3}'.format(row[7], row[8], row[9], row[10])

            Member.objects.update_or_create(
                name = row[2],
                popular_name = row[3],
                defaults = {
                    'accessibility': 1,
                    'rank': '03',
                    'job_title': row[4],
                    'company_name': row[5],
                    'biz_type': row[6],
                    'tel': row[7],
                    'fax': row[8],
                    'zipcode': row[9].strip(),
                    'address': row[10],
                    })
