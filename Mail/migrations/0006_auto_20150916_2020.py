# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mail', '0005_email_receiver'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='date_received',
            new_name='date',
        ),
    ]
