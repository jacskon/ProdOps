# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_pbi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbi',
            name='estimated_finish',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='pbi',
            name='severity',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pbi',
            name='status',
            field=models.CharField(max_length=30),
        ),
    ]
