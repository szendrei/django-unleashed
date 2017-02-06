# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 20:18
from __future__ import unicode_literals

from django.db import migrations
from datetime import datetime

SNIPPETS = [
    {
        'title': 'Hello World',
        'language': 'python',
        'author': 'Dora',
        'create_date': datetime(2017, 1, 21, 12, 12, 31),
        'code': 'print("hello world")',
    },
    {
        'title': '',
        'language': 'html',
        'author': 'Anonymus',
        'create_date': datetime(2017, 1, 23, 6, 1, 35),
        'code': '<p>hello world</p>',
    },
    {
        'title': '',
        'language': 'css',
        'author': 'Anyonymus',
        'create_date': datetime(2017, 1, 26, 14, 0, 0),
        'code': '.wrapper {\n    padding: 10px;\n    magrin: 0;\n}',
    },
    {
        'title': 'user input',
        'language': 'python',
        'author': 'Edit',
        'create_date': datetime(2017, 1, 29, 18, 52, 10),
        'code': 'integer = int(input("Enter digits:"))',
    },
    {
        'title': '',
        'language': 'python',
        'author': 'Anonymus',
        'create_date': datetime(2017, 1, 29, 19, 20, 54),
        'code': 'print("hello")',
    },
    {
        'title': '',
        'language': 'python',
        'author': 'Anyonymus',
        'create_date': datetime(2017, 2, 1, 15, 21, 43),
        'code': 'print("hello")',
    },
    {
        'title': 'hello',
        'language': 'python',
        'author': 'Edit',
        'create_date': datetime(2017, 2, 2, 3, 45, 12),
        'code': 'print("hello")',
    },
    {
        'title': '',
        'language': 'python',
        'author': 'Edit',
        'create_date': datetime(2017, 2, 3, 16, 16, 16),
        'code': 'print("hello")',
    }
]


class Migration(migrations.Migration):

    def add_snippet_data(apps, schema_editor):
        Snippet = apps.get_model('snippets', 'Snippet')
        for snippet in SNIPPETS:
            snippet_object = Snippet.objects.create(
                title=snippet['title'],
                language=snippet['language'],
                author=snippet['author'],
                code=snippet['code'])
            snippet_object.create_date = snippet['create_date']
            snippet_object.save()
    
    def remove_snippet_data(apps, schema_editor):
        Snippet = apps.get_model('snippets', 'Snippet')
        for snippet in SNIPPETS:
            snippet.delete()

    dependencies = [
        ('snippets', '0002_snippet_author'),
    ]

    operations = [
        migrations.RunPython(add_snippet_data, remove_snippet_data)
    ]
