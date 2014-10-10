# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dbcred',
            fields=[
                ('cred_name', models.CharField(max_length=80, serialize=False, primary_key=True)),
                ('database', models.CharField(max_length=80)),
                ('user', models.CharField(max_length=80)),
                ('password', models.CharField(max_length=80)),
                ('host', models.CharField(max_length=80)),
                ('port', models.DateTimeField(max_length=80)),
            ],
            options={
                'db_table': 'db_creds',
            },
            bases=(models.Model,),
        ),
    ]
