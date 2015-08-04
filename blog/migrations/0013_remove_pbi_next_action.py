# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_pbi_update'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pbi',
            name='next_action',
        ),
    ]
