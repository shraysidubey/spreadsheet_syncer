# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assg', '0003_auto_20210114_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.CharField(max_length=120),
        ),
    ]
