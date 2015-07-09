# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sunehaapp', '0002_auto_20150708_0028'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='word',
            name='figureofspeech',
        ),
        migrations.RemoveField(
            model_name='word',
            name='language',
        ),
        migrations.DeleteModel(
            name='figureofspeech',
        ),
        migrations.DeleteModel(
            name='language',
        ),
    ]
