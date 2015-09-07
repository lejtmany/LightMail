# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mail', '0002_mail'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mail',
            new_name='Email',
        ),
    ]
