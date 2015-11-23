# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('usuario_nombre', models.CharField(max_length=60)),
                ('usuario_direccion', models.CharField(max_length=100)),
                ('usuario_correo', models.CharField(max_length=100)),
            ],
        ),
    ]
