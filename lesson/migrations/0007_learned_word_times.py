# Generated by Django 4.0.5 on 2022-12-06 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lesson', '0006_learned_word'),
    ]

    operations = [
        migrations.AddField(
            model_name='learned_word',
            name='times',
            field=models.IntegerField(default=1),
        ),
    ]