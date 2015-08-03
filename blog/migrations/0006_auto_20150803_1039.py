# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_pbi_updates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbi',
            name='updates',
            field=models.TextField(null=True),
        ),
    ]
