# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-26 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='image',
        ),
        migrations.RemoveField(
            model_name='courseresource',
            name='download',
        ),
        migrations.AddField(
            model_name='courseresource',
            name='resource_link',
            field=models.ImageField(default='', upload_to='/upload/%Y%m', verbose_name='\u8d44\u6e90\u6587\u4ef6'),
        ),
        migrations.AddField(
            model_name='video',
            name='video_link',
            field=models.ImageField(default='', upload_to='/upload/%Y%m', verbose_name='\u89c6\u9891\u5730\u5740'),
        ),
        migrations.AlterField(
            model_name='course',
            name='imageFile',
            field=models.ImageField(default='', upload_to='/upload/%Y%m', verbose_name='\u5c01\u9762\u56fe'),
        ),
    ]
