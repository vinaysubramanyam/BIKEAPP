# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0004_auto_20151111_1318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='password',
        ),
    ]
