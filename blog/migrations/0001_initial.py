# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('approved', models.BooleanField(default=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateTimeField(null=True, default=django.utils.timezone.now)),
                ('frequency', models.CharField(max_length=20, choices=[('DAILY', 'Daily'), ('WEEKLY', 'Weekly'), ('FORTNIGHTLY', 'Fortnightly'), ('MONTHLY', 'Monthly')])),
                ('day', models.IntegerField(choices=[(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (7, 'Sunday')])),
                ('start_week', models.IntegerField(choices=[(0, 'N/A'), (1, 'First'), (2, 'Second'), (3, 'Third'), (4, 'Fourth')])),
                ('team', models.TextField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('severity', models.CharField(max_length=30, choices=[('Low', 'Low'), ('Medium', 'Medium'), ('High', 'High'), ('Critical', 'Critical')])),
                ('status', models.CharField(max_length=30, choices=[('In Progress', 'In Progress'), ('Under Investigation', 'Under Investigation'), ('Pending', 'Pending'), ('Assigned', 'Assigned'), ('Closed', 'Closed')])),
                ('assignee', models.CharField(max_length=30)),
                ('estimated_finish', models.DateField(default=django.utils.timezone.now)),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.CharField(max_length=30, choices=[('PBI', 'PBI'), ('Operations', 'Operations')], default='')),
                ('progress_bar', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('task', models.CharField(max_length=60, choices=[('Monday Morning Health Check', 'Monday Morning Health Check'), ('Tuesday Morning Health Check', 'Tuesday Morning Health Check'), ('Wednesday Morning Health Check', 'Wednesday Morning Health Check'), ('Thursday Morning Health Check', 'Thursday Morning Health Check'), ('Friday Morning Health Check', 'Friday Morning Health Check'), ('On call', 'On call'), ('Monday evening Standby', 'Monday evening Standby'), ('Tuesday evening Standby', 'Tuesday evening Standby'), ('Wednesday evening Restarts', 'Wednesday evening Restarts'), ('Thursday evening Standby', 'Thursday evening Standby'), ('Friday evening Standby', 'Friday evening Standby')])),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to='blog.Employee')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('team_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('text', models.TextField()),
                ('update_type', models.CharField(max_length=20, choices=[('Next Action', 'Next Action'), ('Update', 'Update')])),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(related_name='updates', to='blog.Pbi')),
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
            field=models.ForeignKey(related_name='comments', to='blog.Post'),
        ),
    ]
