from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField(max_length=100, verbose_name='Задача')
    description = models.TextField(blank=True, verbose_name='Описание')
    is_complete = models.BooleanField(default=False, verbose_name='Статус')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_done = models.DateTimeField(blank=True, verbose_name='Время выполнения')
    list = models.ForeignKey('TaskList', on_delete=models.CASCADE, verbose_name='В списке')


class TaskList(models.Model):
    name = models.CharField(max_length=100, verbose_name='Список')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
