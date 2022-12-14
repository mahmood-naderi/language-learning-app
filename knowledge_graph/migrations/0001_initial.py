# Generated by Django 4.0.5 on 2022-10-31 10:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', models.CharField(max_length=25)),
                ('meaning', models.CharField(max_length=25)),
                ('weight', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lexical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=25)),
                ('meaning', models.CharField(max_length=25)),
                ('weight', models.IntegerField()),
                ('context1', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='knowledge_graph.context')),
                ('context2', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='context2', to='knowledge_graph.context')),
                ('context3', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='context3', to='knowledge_graph.context')),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listening_weight', models.IntegerField()),
                ('reading_weight', models.IntegerField()),
                ('writing_weight', models.IntegerField()),
                ('word', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='knowledge_graph.lexical')),
            ],
        ),
    ]
