# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20151120_0958'),
        ('cuteblog', '0002_auto_20151116_2315'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('title', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('username', models.ForeignKey(to='account.User')),
            ],
        ),
    ]
