# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='language',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('language_Country', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='word',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('word_text', models.CharField(max_length=250)),
                ('word_meaning', models.CharField(max_length=300)),
            ],
        ),
    ]
