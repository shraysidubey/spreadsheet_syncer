# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('email_address', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('current_city', models.CharField(max_length=200)),
                ('contact_number', models.IntegerField(max_length=50)),
                ('age', models.IntegerField(max_length=120)),
                ('current_or_last_employer', models.CharField(max_length=200)),
                ('job_role', models.CharField(max_length=200)),
                ('current_or_last_CTC', models.FloatField()),
                ('FIXED_component_CTC', models.FloatField()),
                ('work_experience', models.FloatField()),
                ('days_working_in_a_week', models.CharField(max_length=200)),
                ('relocate_to_Mumbai', models.CharField(max_length=200)),
                ('english_communication', models.IntegerField(max_length=11)),
                ('skills', models.CharField(max_length=200)),
                ('previous_industries', models.CharField(max_length=200)),
                ('post_sale_profile', models.CharField(max_length=200)),
                ('select', models.CharField(max_length=200)),
                ('upload_resume', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
