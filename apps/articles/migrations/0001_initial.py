# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.management import call_command
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    def load_data(apps, schema_editor):
        call_command("loaddata", "apps/articles/fixtures/initial.json")

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(editable=False, db_index=True)),
                ('updated_at', models.DateTimeField(editable=False, db_index=True)),
                ('title', models.CharField(max_length=128)),
                ('body', models.TextField()),
                ('slug', models.SlugField(max_length=130)),
                ('is_published', models.BooleanField(default=False)),
                ('published_at', models.DateTimeField(null=True, blank=True)),
                ('show_quote', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'article',
                'verbose_name_plural': 'articles',
            },
        ),
        migrations.CreateModel(
            name='ArticleImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_at', models.DateTimeField(editable=False, db_index=True)),
                ('updated_at', models.DateTimeField(editable=False, db_index=True)),
                ('image', models.ImageField(upload_to=b'articleimages/')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),

        migrations.RunPython(load_data),
    ]
