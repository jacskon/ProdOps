# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150807_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
