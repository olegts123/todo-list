# Generated by Django 4.1.6 on 2023-02-10 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Список')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Задача')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('is_complete', models.BooleanField(default=False, verbose_name='Статус')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('time_done', models.DateTimeField(blank=True, verbose_name='Время выполнения')),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.tasklist', verbose_name='В списке')),
            ],
        ),
    ]