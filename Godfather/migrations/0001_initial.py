# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import Godfather.models
import simple_email_confirmation.models
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_title', models.CharField(max_length=500)),
                ('article_content', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('likes', models.IntegerField(default=0, blank=True)),
                ('author', models.CharField(max_length=50, blank=True)),
                ('image', models.ImageField(upload_to='Images/%Y/%m/%d', blank=True)),
                ('video', embed_video.fields.EmbedVideoField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('country', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password', blank=True)),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(max_length=100, verbose_name='Username', unique=True, db_index=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('joined', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(simple_email_confirmation.models.SimpleEmailConfirmationUserMixin, models.Model),
            managers=[
                ('objects', Godfather.models.MyUserManager()),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='comment',
            field=models.ManyToManyField(to='Godfather.Comment'),
        ),
    ]
