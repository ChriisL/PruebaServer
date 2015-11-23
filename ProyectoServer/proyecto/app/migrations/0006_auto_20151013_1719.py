# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20151013_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='lib_descripcion',
            field=models.TextField(max_length=500),
        ),
    ]
