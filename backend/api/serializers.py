"""Модуль для серилазиаторов api."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Сериализатор для задач."""

    class Meta:
        """Мета инфоомация для сериализатора задач."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
