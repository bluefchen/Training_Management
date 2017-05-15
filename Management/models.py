# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.utils import timezone
# Create your models here.

# people's personal info
class Person(models.Model):
    number = models.CharField(max_length=32, default='1700001', primary_key=True)
    idcard = models.CharField(max_length=32, default='13027472347324')
    province = models.CharField(max_length=32, default='Shanghai')
    name = models.CharField(max_length=32, default='LiHua')
    gender = models.CharField(max_length=1, default='F')
    age = models.CharField(max_length=3, default='25')
    phone = models.CharField(max_length=15, default='18510309110')
    email = models.CharField(max_length=32, default='bigplane@qq.com')
    address = models.CharField(max_length=128, default='上海市嘉定区曹安公路4800号')
    image = models.ImageField(upload_to='avatar', default='avatar/timg.jpg')
    def __unicode__(self):
        return self.name
# trainee grade info
class Grade(models.Model):
    person = models.OneToOneField(Person, related_name='person_grade')
    lesson1 = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    lesson2 = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    lesson3 = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    average = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)

class LessonOne(models.Model):
    number = models.CharField(max_length=32, default='1700001')
    level1 = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    level2 = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    level3 = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    level4 = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    level5 = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    average = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    train_time = models.DateTimeField(auto_now=True)

class Avatar(models.Model):
    number = models.CharField(max_length=32, default='1700001', primary_key=True)
    image = models.ImageField(upload_to='avatar', blank=True, null=True)