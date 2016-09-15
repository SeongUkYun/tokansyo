from django.contrib import admin

from models import recruit as Recruit

@admin.register(Recruit)
class recruitAdmin(admin.ModelAdmin):
    list_display = ['work_type', 'employment_type', 'start_date', 'end_date']

    list_filter = ['employment_type']
