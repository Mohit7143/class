# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-28 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0002_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='demomodel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
    ]
