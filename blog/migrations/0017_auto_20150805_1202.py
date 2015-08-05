# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_pbi_progress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbi',
            name='progress',
            field=models.IntegerField(null=True),
        ),
    ]
