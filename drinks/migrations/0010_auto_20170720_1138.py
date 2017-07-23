# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-20 11:38
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drinks', '0009_auto_20170708_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', ckeditor.fields.RichTextField(default='')),
            ],
        ),
        migrations.DeleteModel(
            name='group',
        ),
        migrations.AddField(
            model_name='article',
            name='Date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=ckeditor.fields.RichTextField(default=''),
        ),
        migrations.AddField(
            model_name='comment',
            name='Art',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drinks.Article'),
        ),
        migrations.AddField(
            model_name='comment',
            name='admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]