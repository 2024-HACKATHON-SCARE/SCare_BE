# Generated by Django 5.0.7 on 2024-07-20 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_is_child_user_is_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_child',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_parent',
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('child', '자녀'), ('parent', '부모')], default=1, max_length=10),
            preserve_default=False,
        ),
    ]