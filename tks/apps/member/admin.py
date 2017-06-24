from django.contrib import admin

from models import member as Member
from models import Historicalmember


@admin.register(Member)
class memberAdmin(admin.ModelAdmin):
    list_display = ['name', 'biz_type', 'company_name',
                    'tel', 'fax', 'zipcode', 'address', 'url',
                    'home_tel', 'home_fax', 'home_zipcode', 'home_address']


@admin.register(Historicalmember)
class HistoricalmemberAdmin(admin.ModelAdmin):
    ordering = ('name', 'history_date')
    list_filter = ('name', )
    list_display = ['name', 'rank', 'history_date', 'history_user']
