# Generated by Django 4.0.5 on 2022-12-07 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge_graph', '0004_alter_lexical_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='context',
            name='weight',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='lexical',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]