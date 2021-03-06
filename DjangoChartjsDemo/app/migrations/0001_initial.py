# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-31 16:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=255)),
                ('reading', models.IntegerField()),
            ],
            options={
                'ordering': ('-date', 'name'),
            },
        ),
    ]
