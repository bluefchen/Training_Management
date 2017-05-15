# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from models import *
import json
from forms import *
import os
from django.conf import settings
import time
# 首页
def index(request):
    person = Person.objects.get(pk=1)
    return render(request, 'manage/index.html', {'person': person})

#  得到培训人员的列表
def peoplelist(request):
    people = Person.objects.order_by('number')
    return render(request, 'manage/people.html', {'people': people})

#  得到某一个培训人员的具体信息
def person(request, id):
    person = Person.objects.get(number=id)
    grade = person.person_grade
    lesson1 = grade.lesson1;
    lesson2 = grade.lesson2;
    lesson3 = grade.lesson3;
    lessons = [{'name':'lesson1', 'value':str(lesson1)}, {'name':'lesson2', 'value':str(lesson2)}, {'name':'lesson3', 'value':str(lesson3)}]
    return render(request, 'manage/person.html', {'person': person, 'grade': json.dumps(lessons)})

#  新建或者修改一个培训人员的具体信息
def edit_person(request, id):
    if str(id) == '0':
        person = Person(number="0", name="", province="", idcard="", gender="", age="", phone="", email="", address="")
    else:
        person = Person.objects.get(number=id)
    return render(request, 'manage/person_edit.html', {'person': person})

# 更新培训人员个人信息
def update_person(request):
    receive_data = request.POST
    number = receive_data['number']
    person = Person()
    print 'number is '+number
    if str(number) == '0':
        year = time.strftime("%y", time.localtime(time.time()))
        number = int(year)*10000 + len(Person.objects.all()) + 1
        person.number = number
        grade = person.person_grade;
        grade.lesson1 = 60.00;
        grade.lesson2 = 60.00;
        grade.lesson3 = 60.00;
        grade.average = 60.00;
        grade.save();
    else:
        person = Person.objects.get(number=number)
    person.name = receive_data['name']
    person.idcard = receive_data['idcard']
    person.province = receive_data['province']
    person.gender = receive_data['gender']
    person.age = receive_data['age']
    person.phone = receive_data['phone']
    person.email = receive_data['email']
    person.address = receive_data['address']
    if 'avatar' in request.FILES:
         path = settings.MEDIA_ROOT
         file_name = 'avatar/'+number+".jpg"
         file = os.path.join(path, file_name)
         print file
         if os.path.exists(file):
             os.remove(file)
         avatar = request.FILES['avatar']
         avatar.name = number+".jpg"
         person.image = avatar
    person.save();
    return HttpResponseRedirect('/manage/person/'+number);

# 培训系统上传学员培训数据
def setLessonOneGrade(request):
    if request.POST:
        receive_data = request.POST
        s_number = request.POST['number']
        s_level1 = float(request.POST['level1'])
        s_level2 = float(request.POST['level2'])
        s_level3 = float(request.POST['level3'])
        s_level4 = float(request.POST['level4'])
        s_level5 = float(request.POST['level5'])
        # compute the average for lesson1
        s_average = str((s_level1 + s_level2 + s_level3 + s_level4 + s_level5)/5)
        person = Person.objects.get(number=s_number)
        # update grade table lesson one date and average evaluate
        grade = person.person_grade
        s_lesson_average = (float(grade.average) * 3 - float(grade.lesson1) + float(s_average))/3
        grade.lesson1 = s_average
        grade.average = s_lesson_average
        grade.save()
        # add a new recored for lesson1
        lesson1 = LessonOne(number=s_number, level1=str(s_level1), level2=str(s_level2), level3=str(s_level3),
                            level4=str(s_level4), level5=s_level5)
        lesson1.save()
        return HttpResponse('1')
    else:
        return HttpResponse('0')

