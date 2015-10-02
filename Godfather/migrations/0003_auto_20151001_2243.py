# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Godfather', '0002_myuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(upload_to='Images/%Y/%m/%d', blank=True, width_field=200, height_field=200),
        ),
    ]
