# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assg', '0005_auto_20210114_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='timestamp',
            field=models.CharField(max_length=200),
        ),
    ]
