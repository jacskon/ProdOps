# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20150804_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='pbi',
            name='progress',
            field=models.IntegerField(default=1),
        ),
    ]
