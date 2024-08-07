# Generated by Django 5.0.7 on 2024-07-23 12:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Day',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_code', models.CharField(choices=[('MO', '월'), ('TU', '화'), ('WE', '수'), ('TH', '목'), ('FR', '금'), ('SA', '토'), ('SU', '일')], max_length=2, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('due_date', models.DateField(blank=True, null=True)),
                ('due_time', models.TimeField(blank=True, null=True)),
                ('completed', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('repeat_on', models.ManyToManyField(blank=True, to='checklist.day')),
                ('shared_with', models.ManyToManyField(blank=True, related_name='shared_todos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
