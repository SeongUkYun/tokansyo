from django.contrib import admin

from models import news as News


@admin.register(News)
class newsAdmin(admin.ModelAdmin):
    list_display = ['title', 'news_type']

    list_filter = ['news_type',]
