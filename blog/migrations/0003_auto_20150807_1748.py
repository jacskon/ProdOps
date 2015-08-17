# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_update_test_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pbi',
            old_name='progress_bar',
            new_name='progressing_bar',
        ),
    ]
