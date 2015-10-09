# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mail', '0007_email_is_read'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='email',
            options={'ordering': ['date']},
        ),
    ]
