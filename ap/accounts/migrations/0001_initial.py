# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('terms', '__first__'),
        ('houses', '__first__'),
        ('services', '__first__'),
        ('localities', '__first__'),
        ('auth', '0006_require_contenttypes_0002'),
        ('teams', '__first__'),
        ('aputils', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name='email address', db_index=True)),
                ('firstname', models.CharField(max_length=30, verbose_name='first name')),
                ('lastname', models.CharField(max_length=30, verbose_name='last name')),
                ('middlename', models.CharField(max_length=30, null=True, verbose_name='middle name', blank=True)),
                ('nickname', models.CharField(max_length=30, null=True, blank=True)),
                ('maidenname', models.CharField(max_length=30, null=True, verbose_name='maiden name', blank=True)),
                ('gender', models.CharField(max_length=1, choices=[(b'B', b'Brother'), (b'S', b'Sister')])),
                ('date_of_birth', models.DateField(null=True)),
                ('phone', models.CharField(max_length=25, null=True, blank=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('type', models.CharField(max_length=1, choices=[(b'R', b'Regular (full-time)'), (b'S', b'Short-term (long-term)'), (b'C', b'Commuter')])),
                ('date_begin', models.DateField()),
                ('date_end', models.DateField(null=True, blank=True)),
                ('married', models.BooleanField(default=False)),
                ('self_attendance', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TrainingAssistant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('active', models.BooleanField(default=True)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('account', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
                ('houses', models.ManyToManyField(to='houses.House', blank=True)),
                ('services', models.ManyToManyField(to='services.Service', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='trainee',
            name='TA',
            field=models.ForeignKey(blank=True, to='accounts.TrainingAssistant', null=True),
        ),
        migrations.AddField(
            model_name='trainee',
            name='account',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='trainee',
            name='address',
            field=models.ForeignKey(verbose_name=b'home address', blank=True, to='aputils.Address', null=True),
        ),
        migrations.AddField(
            model_name='trainee',
            name='bunk',
            field=models.ForeignKey(blank=True, to='houses.Bunk', null=True),
        ),
        migrations.AddField(
            model_name='trainee',
            name='house',
            field=models.ForeignKey(blank=True, to='houses.House', null=True),
        ),
        migrations.AddField(
            model_name='trainee',
            name='locality',
            field=models.ManyToManyField(to='localities.Locality'),
        ),
        migrations.AddField(
            model_name='trainee',
            name='mentor',
            field=models.ForeignKey(related_name='mentee', blank=True, to='accounts.Trainee', null=True),
        ),
        migrations.AddField(
            model_name='trainee',
            name='spouse',
            field=models.OneToOneField(null=True, blank=True, to='accounts.Trainee'),
        ),
        migrations.AddField(
            model_name='trainee',
            name='team',
            field=models.ForeignKey(blank=True, to='teams.Team', null=True),
        ),
        migrations.AddField(
            model_name='trainee',
            name='term',
            field=models.ManyToManyField(to='terms.Term'),
        ),
    ]
