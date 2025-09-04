"""Модуль конфига для приложения Api."""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Конфиг для приложеня Api."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
