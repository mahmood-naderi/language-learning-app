# Generated by Django 4.0.5 on 2022-12-06 16:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0002_mistake'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mistake',
            name='context',
        ),
    ]