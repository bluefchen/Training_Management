# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 10:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson1', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('lesson2', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('lesson3', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('average', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='LessonOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='1700001', max_length=32)),
                ('level1', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('level2', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('level3', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('level4', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('level5', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('average', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('train_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LessonThree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='1700001', max_length=32)),
                ('level1', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('level2', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('level3', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('level4', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('level5', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('level6', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('average', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('train_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='LessonTwo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(default='1700001', max_length=32)),
                ('level1', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('level2', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('level3', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('average', models.DecimalField(decimal_places=2, default=60.0, max_digits=5)),
                ('train_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('number', models.CharField(default='1700001', max_length=32, primary_key=True, serialize=False)),
                ('idcard', models.CharField(default='13027472347324', max_length=32)),
                ('province', models.CharField(default='Shanghai', max_length=32)),
                ('name', models.CharField(default='LiHua', max_length=32)),
                ('gender', models.CharField(default='F', max_length=2)),
                ('age', models.CharField(default='25', max_length=3)),
                ('phone', models.CharField(default='18510309110', max_length=15)),
                ('email', models.CharField(default='bigplane@qq.com', max_length=32)),
                ('address', models.CharField(default='\u4e0a\u6d77\u5e02\u5609\u5b9a\u533a\u66f9\u5b89\u516c\u8def4800\u53f7', max_length=128)),
                ('image', models.ImageField(default='pictures/timg.jpg', upload_to='pictures')),
            ],
        ),
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='admin', max_length=32)),
                ('password', models.CharField(default='admin', max_length=32)),
            ],
        ),
        migrations.AddField(
            model_name='grade',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='person_grade', to='Management.Person'),
        ),
    ]
