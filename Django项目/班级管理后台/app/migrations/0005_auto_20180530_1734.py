# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-30 09:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_grade2_student2_stuinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student2',
            name='g',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Grade2'),
        ),
        migrations.AlterField(
            model_name='stuinfo',
            name='stu',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app.Student2'),
        ),
    ]
