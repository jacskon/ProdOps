# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20150805_1231'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pbi',
            name='state',
        ),
        migrations.AlterField(
            model_name='pbi',
            name='status',
            field=models.CharField(max_length=30, choices=[('In Progress', 'In Progress'), ('Under Investigation', 'Under Investigation'), ('Pending', 'Pending'), ('Assigned', 'Assigned'), ('Closed', 'Closed')]),
        ),
    ]
