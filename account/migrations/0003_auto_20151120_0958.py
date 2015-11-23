# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20151120_0942'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='username',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
    ]
