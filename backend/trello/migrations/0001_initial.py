# Generated by Django 3.1.7 on 2021-04-01 08:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrelloBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('trello_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrelloLabel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('trello_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrelloList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('trello_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('trello_board',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trello.trelloboard')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrelloCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField()),
                ('trello_id', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField(blank=True, null=True)),
                ('points_estimated', models.FloatField(blank=True, default=0, null=True)),
                ('points_consumed_extra', models.FloatField(blank=True, default=0, null=True)),
                ('trello_labels', models.ManyToManyField(blank=True, to='trello.TrelloLabel')),
                ('trello_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trello.trellolist')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]