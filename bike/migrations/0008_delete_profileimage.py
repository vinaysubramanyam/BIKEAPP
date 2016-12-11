# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0007_link_vote'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfileImage',
        ),
    ]
