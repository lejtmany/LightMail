# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mail', '0004_auto_20150907_0258'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='receiver',
            field=models.CharField(max_length=50, default='default@default.com'),
            preserve_default=False,
        ),
    ]
