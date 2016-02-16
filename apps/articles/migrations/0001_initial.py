# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

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
                ('published_at', models.DateTimeField(null=True, blank=True))
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
    ]
