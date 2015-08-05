# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20150805_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbi',
            name='progress_bar',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
