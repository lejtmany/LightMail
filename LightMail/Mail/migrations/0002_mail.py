# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mail', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('date_recieved', models.DateTimeField()),
                ('sender', models.CharField(max_length=50)),
                ('subject', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('is_deleted', models.BooleanField()),
            ],
        ),
    ]
