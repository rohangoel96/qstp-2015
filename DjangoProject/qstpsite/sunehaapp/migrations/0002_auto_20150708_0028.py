# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sunehaapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='figureofspeech',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('figureofspeech_text', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='word',
            name='language',
            field=models.ForeignKey(to='sunehaapp.language', null=b'TRUE'),
        ),
        migrations.AddField(
            model_name='word',
            name='figureofspeech',
            field=models.ForeignKey(to='sunehaapp.figureofspeech', null=b'TRUE'),
        ),
    ]
