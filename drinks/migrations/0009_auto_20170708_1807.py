# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-08 18:07
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0008_article_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
