# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20150805_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='pbi',
            name='test',
            field=models.CharField(default='test', max_length=10),
            preserve_default=False,
        ),
    ]
