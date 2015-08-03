# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20150803_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pbi',
            name='update',
        ),
    ]
