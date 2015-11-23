# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lib_imagen', models.ImageField(upload_to=b'libros/')),
                ('lib_titulo', models.CharField(max_length=60)),
                ('lib_autor', models.CharField(max_length=60)),
                ('lib_categoria', models.CharField(max_length=60)),
                ('lib_descripcion', models.CharField(max_length=60)),
                ('lib_fecha', models.DateField()),
            ],
        ),
    ]
