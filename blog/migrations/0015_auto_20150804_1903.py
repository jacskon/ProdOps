# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_pbi_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbi',
            name='state',
            field=models.CharField(default='Open', max_length=10, choices=[('Open', 'Open'), ('Closed', 'Closed')]),
        ),
    ]
