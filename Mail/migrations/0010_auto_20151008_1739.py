# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mail', '0009_auto_20151008_1738'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'ordering': ['date']},
        ),
    ]
