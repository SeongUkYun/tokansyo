from django.contrib import admin

from models import gallery as Gallery

@admin.register(Gallery)
class galleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image', 'name', 'descript', 'created_at', 'updated_at']
    list_filter = ['created_at']
