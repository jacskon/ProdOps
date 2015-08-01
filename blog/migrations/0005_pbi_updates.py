# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20150801_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='pbi',
            name='updates',
            field=models.TextField(default='Initial update'),
            preserve_default=False,
        ),
    ]
