# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('importings', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dbcred',
            name='port',
            field=models.CharField(max_length=80),
        ),
    ]
