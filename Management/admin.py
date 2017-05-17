# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from models import *

# Register your models here.

# admin.site.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('number', 'name')
    list_filter = ('number',)

admin.site.register(Person, PersonAdmin)

class GradeAdmin(admin.ModelAdmin):
    list_display = ('person', 'lesson1', 'lesson2','lesson3', 'average')

admin.site.register(Grade, GradeAdmin)

class LessonOneAdmin(admin.ModelAdmin):
    list_display = ('number', 'level1', 'level2','level3', 'level4', 'level5', 'average', 'train_time')

admin.site.register(LessonOne, LessonOneAdmin)

class LessonTwoAdmin(admin.ModelAdmin):
    list_display = ('number', 'level1', 'level2','level3', 'average', 'train_time')

admin.site.register(LessonTwo, LessonTwoAdmin)

class LessonThreeAdmin(admin.ModelAdmin):
    list_display = ('number', 'level1', 'level2','level3', 'level4', 'level5','level6', 'average', 'train_time')

admin.site.register(LessonThree, LessonThreeAdmin)

class SuperUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')

admin.site.register(SuperUser, SuperUserAdmin)