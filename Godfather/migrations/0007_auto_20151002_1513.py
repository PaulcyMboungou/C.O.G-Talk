# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Godfather', '0006_auto_20151001_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(default='media/default/picture.jpg', upload_to='Images/Profile Pictures', blank=True),
        ),
    ]
