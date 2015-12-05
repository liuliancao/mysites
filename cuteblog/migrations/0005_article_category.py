# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuteblog', '0004_auto_20151120_1028'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.TextField(max_length=30, null=True),
        ),
    ]
