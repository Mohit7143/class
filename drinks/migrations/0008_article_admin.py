# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-02 19:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0007_auto_20170629_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='admin',
            field=models.IntegerField(default=1),
        ),
    ]