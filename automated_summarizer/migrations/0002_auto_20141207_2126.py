# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('automated_summarizer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='eulainput',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 7, 21, 26, 20, 139177, tzinfo=utc), verbose_name=b'date published', auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='eulainput',
            name='last_update_datetime',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 7, 21, 26, 32, 15411, tzinfo=utc), verbose_name=b'date/time of last edit', auto_now=True),
            preserve_default=False,
        ),
    ]
