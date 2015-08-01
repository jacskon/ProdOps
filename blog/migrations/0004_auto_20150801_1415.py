# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_pbi_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='pbi',
            name='title',
            field=models.CharField(default='Title', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pbi',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='pbi',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]
