# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assg', '0002_auto_20210114_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='contact_number',
            field=models.CharField(max_length=50),
        ),
    ]
