# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20150725_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='team',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pbi',
            name='status',
            field=models.CharField(max_length=30, choices=[('In Progress', 'In Progress'), ('Under Investigation', 'Under Investigation'), ('Pending', 'Pending'), ('Assigned', 'Assigned')]),
        ),
    ]
