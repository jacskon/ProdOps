# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20150725_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pbi',
            name='status',
            field=models.CharField(max_length=30, choices=[('IN_PROGRESS', 'In Progress'), ('UNDER_INVESTIGATION', 'Under Investigation'), ('PENDING', 'Pending'), ('ASSIGNED', 'Assigned')]),
        ),
    ]
