from django.contrib import admin

from models import member as Member

@admin.register(Member)
class memberAdmin(admin.ModelAdmin):
    list_display = ['name', 'biz_type', 'company_name', 'tel', 'fax', 'zipcode', 'address', 'url']
