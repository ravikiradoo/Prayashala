# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-21 13:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PrayaShala', '0012_auto_20170610_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='Image',
            field=models.FileField(default='static/PrayaShala/noImage.png', upload_to='Questions'),
        ),
    ]
