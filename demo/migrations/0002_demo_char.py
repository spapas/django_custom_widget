# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-03 21:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='demo',
            name='char',
            field=models.CharField(choices=[('CH1', 'Choice 1'), ('CH2', 'Choice 2'), ('CH3', 'Choice 3'), ('CH4', 'Choice 4')], default='a', max_length=16),
            preserve_default=False,
        ),
    ]
