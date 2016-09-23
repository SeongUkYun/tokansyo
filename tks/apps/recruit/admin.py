from django.contrib import admin

from models import recruit as Recruit

@admin.register(Recruit)
class recruitAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'status', 'start_date', 'end_date']

    list_filter = ['status']
