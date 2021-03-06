# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-06 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0035_auto_20181215_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backend',
            name='predicateName',
            field=models.TextField(blank=True, default='', help_text='Relation that tells QLever UI the name of a predicate (without prefixes).', verbose_name='Predicate name relation'),
        ),
        migrations.AlterField(
            model_name='link',
            name='content',
            field=models.TextField(),
        ),
    ]
