# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-28 18:10
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0005_remove_group_grp_cont'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='XYZ', max_length=200),
        ),
        migrations.AddField(
            model_name='group',
            name='grp_admin',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='group',
            name='grp_cont',
            field=models.CharField(default='XYZ', max_length=1500),
        ),
        migrations.AddField(
            model_name='group',
            name='grp_title',
            field=models.CharField(default='XYZ', max_length=200),
        ),
    ]
