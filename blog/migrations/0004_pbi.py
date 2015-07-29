# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150714_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pbi',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('number', models.IntegerField()),
                ('description', models.CharField(max_length=30)),
                ('severity', models.TextField()),
                ('status', models.TextField()),
                ('assignee', models.CharField(max_length=30)),
                ('estimated_finish', models.DateTimeField(default=django.utils.timezone.now)),
                ('next_action', models.CharField(max_length=30)),
            ],
        ),
    ]
