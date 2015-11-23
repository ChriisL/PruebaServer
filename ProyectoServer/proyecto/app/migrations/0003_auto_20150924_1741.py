# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_libros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='lib_categoria',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='libros',
            name='lib_descripcion',
            field=models.CharField(max_length=200),
        ),
    ]
