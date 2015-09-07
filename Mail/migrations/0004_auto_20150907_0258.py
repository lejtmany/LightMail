# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mail', '0003_auto_20150907_0249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='date_recieved',
            new_name='date_received',
        ),
    ]
