"""Настройки для админ панели."""
from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Админ панель для задач."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
