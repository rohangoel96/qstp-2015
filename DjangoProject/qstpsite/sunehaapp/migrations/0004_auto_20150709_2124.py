# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sujithapp', '0001_initial'),
        ('sunehaapp', '0003_auto_20150709_2123'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='figureofspeech',
            field=models.ForeignKey(to='sujithapp.figureofspeech', null=b'TRUE'),
        ),
        migrations.AddField(
            model_name='word',
            name='language',
            field=models.ForeignKey(to='sujithapp.language', null=b'TRUE'),
        ),
    ]
