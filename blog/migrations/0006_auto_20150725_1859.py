# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20150725_1748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbi',
            name='severity',
            field=models.CharField(choices=[('Low', 'LOW'), ('Medium', 'MEDIUM'), ('High', 'HIGH'), ('Critical', 'CRITICAL')], max_length=30),
        ),
    ]
