# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assg', '0004_auto_20210114_1720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='FIXED_component_CTC',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='current_or_last_CTC',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='employee',
            name='email_address',
            field=models.EmailField(max_length=254, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='english_communication',
            field=models.CharField(max_length=11),
        ),
        migrations.AlterField(
            model_name='employee',
            name='work_experience',
            field=models.CharField(max_length=200),
        ),
    ]
