# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_pbi_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pbi',
            name='test',
        ),
        migrations.AlterField(
            model_name='pbi',
            name='progress_bar',
            field=models.IntegerField(default=10),
            preserve_default=False,
        ),
    ]
