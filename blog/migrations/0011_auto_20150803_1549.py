# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_auto_20150803_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('update_type', models.CharField(choices=[('Next Action', 'Next Action'), ('Update', 'Update')], max_length=20)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='pbi',
            old_name='updates',
            new_name='update',
        ),
        migrations.AddField(
            model_name='update',
            name='task',
            field=models.ForeignKey(to='blog.Pbi', related_name='updates'),
        ),
    ]
