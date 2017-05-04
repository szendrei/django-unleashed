# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_fields_startups_and_tags_optional'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-pub_date', 'title'], 'permissions': (('view_future_post', 'Can view unpublished Post'),), 'get_latest_by': 'pub_date', 'verbose_name': 'blog post'},
        ),
    ]
