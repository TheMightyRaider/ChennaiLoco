# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-01 05:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('train', '0003_auto_20170331_1515'),
    ]

    operations = [
        migrations.AddField(
            model_name='train',
            name='line',
            field=models.CharField(default='north', max_length=5),
            preserve_default=False,
        ),
    ]
