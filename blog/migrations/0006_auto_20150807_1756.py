# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_update'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pbi',
            old_name='progressing_bar',
            new_name='progress_bar',
        ),
        migrations.RemoveField(
            model_name='update',
            name='test_text',
        ),
    ]
