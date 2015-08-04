# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_remove_pbi_next_action'),
    ]

    operations = [
        migrations.AddField(
            model_name='pbi',
            name='state',
            field=models.CharField(default='Open', choices=[('Open', 'Open'), ('Closed', 'Closed')], max_length=10),
            preserve_default=False,
        ),
    ]
