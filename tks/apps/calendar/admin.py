from django.contrib import admin

from models import task as Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'task_date', 'title']
