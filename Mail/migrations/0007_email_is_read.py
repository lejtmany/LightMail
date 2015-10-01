# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mail', '0006_auto_20150916_2020'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='is_read',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
