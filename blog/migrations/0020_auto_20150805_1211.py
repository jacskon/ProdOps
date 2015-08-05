# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_pbi_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pbi',
            old_name='progress',
            new_name='progress_bar',
        ),
    ]
