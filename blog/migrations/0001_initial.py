# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved', models.BooleanField(default=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now, null=True)),
                ('frequency', models.CharField(choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('FORTNIGHTLY', 'Fortnightly'), ('MONTHLY', 'Monthly')], max_length=20)),
                ('day', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('start_week', models.IntegerField(choices=[(0, 'N/A'), (1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')])),
                ('team', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('parameters', models.TextField()),
                ('target', models.CharField(max_length=200)),
                ('target_type', models.CharField(max_length=200)),
                ('credentials', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pbi',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('number', models.IntegerField()),
                ('description', models.CharField(max_length=30)),
                ('severity', models.CharField(choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')], max_length=30)),
                ('status', models.CharField(choices=[('In Progress', 'In Progress'), ('Under Investigation', 'Under Investigation'), ('Pending', 'Pending'), ('Assigned', 'Assigned')], max_length=30)),
                ('assignee', models.CharField(max_length=30)),
                ('estimated_finish', models.DateField(default=django.utils.timezone.now)),
                ('next_action', models.CharField(max_length=30)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(default='', choices=[('PBI', 'PBI'), ('Operations', 'Operations')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('task', models.CharField(choices=[('Monday Morning Health Check', 'Monday Morning Health Check'), ('Tuesday Morning Health Check', 'Tuesday Morning Health Check'), ('Wednesday Morning Health Check', 'Wednesday Morning Health Check'), ('Thursday Morning Health Check', 'Thursday Morning Health Check'), ('Friday Morning Health Check', 'Friday Morning Health Check'), ('On call', 'On call'), ('Monday evening Standby', 'Monday evening Standby'), ('Tuesday evening Standby', 'Tuesday evening Standby'), ('Wednesday evening Restarts', 'Wednesday evening Restarts'), ('Thursday evening Standby', 'Thursday evening Standby'), ('Friday evening Standby', 'Friday evening Standby')], max_length=60)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to='blog.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('team_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='employee',
            name='team',
            field=models.ForeignKey(to='blog.Team'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post', related_name='comments'),
        ),
    ]
