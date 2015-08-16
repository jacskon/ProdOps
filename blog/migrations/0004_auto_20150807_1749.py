# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20150807_1748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='author',
        ),
        migrations.RemoveField(
            model_name='update',
            name='task',
        ),
        migrations.DeleteModel(
            name='Update',
        ),
    ]
