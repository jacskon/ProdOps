# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150803_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbi',
            name='number',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
