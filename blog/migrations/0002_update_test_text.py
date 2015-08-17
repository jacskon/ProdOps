# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='update',
            name='test_text',
            field=models.TextField(default='Test'),
            preserve_default=False,
        ),
    ]
