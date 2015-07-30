# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20150728_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('task', models.CharField(max_length=50, choices=[('Monday Morning Health Check', 'Monday Morning Health Check'), ('Tuesday Morning Health Check', 'Tuesday Morning Health Check'), ('Wednesday Morning Health Check', 'Wednesday Morning Health Check'), ('Thursday Morning Health Check', 'Thursday Morning Health Check'), ('Friday Morning Health Check', 'Friday Morning Health Check'), ('On call', 'On call'), ('Monday evening Standby', 'Monday evening Standby'), ('Tuesday evening Standby', 'Tuesday evening Standby'), ('Wednesday evening Restarts', 'Wednesday evening Restarts'), ('Thursday evening Standby', 'Thursday evening Standby'), ('Friday evening Standby', 'Friday evening Standby')])),
                ('modified_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(to='blog.Employee')),
            ],
        ),
    ]
