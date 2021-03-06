# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-05 16:48
from __future__ import unicode_literals

from datetime import date
from django.db import migrations

POEMS = [
    {
        'title':'Blah',
        'author':'John Swift',
        'slug': 'blah',
        'pub_date':date(2015, 10, 31),
        'text': 'Blah\nBlah\nBlah\n',
        'category': 'absurd',
        },
    {
        'title':'Romantic Serenade',
        'author':'Agatha',
        'slug': 'romantic-serenade',
        'pub_date':date(2016, 1, 1),
        'text': "I'm so romantical\nI can't handle it.",
        'category': 'romantic',
        },
    {
        'title':'Ode to Myself',
        'author':'Agatha',
        'slug': 'ode-to-myself',
        'pub_date':date(2017, 2, 1),
        'text': "It's an ode\nTo a very special person:\nME!",
        'category': 'ode',
        },
]

class Migration(migrations.Migration):

    def add_poem_data(apps, schema_editor):
        Poem = apps.get_model('poems', 'Poem')
        Category = apps.get_model('categories', 'Category')
        for poem in POEMS:
            poem_dict = Poem.objects.create(
                title=poem['title'],
                author=poem['author'],
                slug=poem['slug'],
                text=poem['text'],
                category=Category.objects.get(slug=poem['category']))
            poem_dict.pub_date=poem['pub_date']
            poem_dict.save()            

    def remove_poem_data(apps, schema_editor):
        Poem = apps.get_model('poems', 'Poem')
        for poem in POEMS:
            poem_object = Poem.objects.get(slug=poem['slug'])
            poem_object.delete()

    dependencies = [
        ('poems', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_poem_data, remove_poem_data)
    ]
