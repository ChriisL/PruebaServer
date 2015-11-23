# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150930_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='lib_autor',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='libros',
            name='lib_descripcion',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='libros',
            name='lib_titulo',
            field=models.CharField(max_length=200),
        ),
    ]
