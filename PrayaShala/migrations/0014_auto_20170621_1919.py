# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-21 13:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrayaShala', '0013_auto_20170621_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='Image',
            field=models.FileField(default='/static/PrayaShala/noImage.png', upload_to='Questions'),
        ),
    ]
