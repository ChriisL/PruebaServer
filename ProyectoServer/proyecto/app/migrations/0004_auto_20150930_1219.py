# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150924_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='libros',
            name='lib_descargar',
            field=models.CharField(default=datetime.datetime(2015, 9, 30, 19, 19, 13, 560463, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='libros',
            name='lib_ver',
            field=models.CharField(default=datetime.datetime(2015, 9, 30, 19, 19, 23, 280969, tzinfo=utc), max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='libros',
            name='lib_fecha',
            field=models.DateField(auto_now_add=True),
        ),
    ]
