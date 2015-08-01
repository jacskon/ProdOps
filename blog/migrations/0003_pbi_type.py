# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_pbi_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='pbi',
            name='type',
            field=models.CharField(default='', choices=[('PBI', 'PBI'), ('Operations', 'Operations')], max_length=30),
        ),
    ]
