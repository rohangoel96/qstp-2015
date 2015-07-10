# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rohanapp', '0004_remove_userprofile_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='username',
            field=models.ForeignKey(to='rohanapp.LoginProfile', null=b'FALSE'),
        ),
    ]
