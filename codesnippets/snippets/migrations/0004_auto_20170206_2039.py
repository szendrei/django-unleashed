# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_snippet_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='author',
            field=models.CharField(blank=True, default='Anonymus', max_length=32),
        ),
    ]