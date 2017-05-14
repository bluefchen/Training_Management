# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

# people's personal info
class Person(models.Model):
    number = models.CharField(max_length=32, default='1700001')
    name = models.CharField(max_length=32, default='LiHua')
    gender = models.CharField(max_length=1, default='F')
    age = models.DecimalField(max_digits=3, decimal_places=0, default=25)
    phone = models.DecimalField(max_digits=15, decimal_places=0, null=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=128, default='上海市嘉定区曹安公路4800号')
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
    number = models.CharField(max_length=32, default='135300100')
    level1 = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    level2 = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    level3 = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    level4 = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    level5 = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    average = models.DecimalField(max_digits=5, decimal_places=2, default=60.00)
    train_time = models.DateTimeField(auto_now=True)