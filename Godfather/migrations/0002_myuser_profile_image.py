# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Godfather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='Images/%Y/%m/%d'),
        ),
    ]
