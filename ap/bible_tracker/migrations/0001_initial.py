# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20150530_1616'),
    ]

    operations = [
        migrations.CreateModel(
            name='Daily',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('status', models.CharField(max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstYear', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=100), blank=True)),
                ('secondYear', django.contrib.postgres.fields.ArrayField(size=None, null=True, base_field=models.CharField(max_length=100), blank=True)),
                ('trainee', models.ForeignKey(to='accounts.Trainee', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weekly',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('finalize', models.IntegerField(default=0)),
                ('trainee', models.ForeignKey(to='accounts.Trainee', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='daily',
            name='week',
            field=models.ForeignKey(to='bible_tracker.Weekly'),
        ),
    ]
