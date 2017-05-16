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
    return render(request, 'manage/index.html')
#重置密码
def password(request):
    return render(request,'manage/reset_password.html')
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
# 删除学员信息
def delete_person(request, id):
    print 'delete person'
    person = Person.objects.get(number=id)
    person.delete()
    return HttpResponseRedirect('/manage/people')

# 更新培训人员个人信息
def update_person(request):
    receive_data = request.POST
    number = receive_data['number']
    person = Person()
    print 'number is '+number
    if str(number) == '0':
        year = time.strftime("%y", time.localtime(time.time()))
        number = int(year)*100000 + len(Person.objects.all()) + 1
        person.number = str(number)
        person.save();
        grade = Grade();
        grade.person = person;
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
         avatar = request.FILES['avatar']
         if avatar != None:
             path = settings.MEDIA_ROOT
             file_name = 'avatar/'+str(number)+".jpg"
             file = os.path.join(path, file_name)
             print file
             if os.path.exists(file):
                 os.remove(file)
             avatar.name = str(number)+".jpg"
             person.image = avatar
    person.save();
    return HttpResponseRedirect('/manage/person/'+str(number));

# 具体课程成绩分析
# 反馈的数据格式
# var mdata = [{key:"level1",value:[{date:"day1",key:"level1",value:"90"},{date:"day2",key:"level1",value:"80"},{date:"day3",key:"level1",value:"70"}]}
#         ,{key:"level2",value:[{date:"day1",key:"level2",value:"70"},{date:"day2",key:"level2",value:"80"},{date:"day3",key:"level2",value:"90"}]}
#         ,{key:"level3",value:[{date:"day1",key:"level3",value:"60"},{date:"day2",key:"level3",value:"60"},{date:"day3",key:"level3",value:"60"}]}]
def lesson_analysis(request,lesson, id):
    if str(lesson) =='lesson1':
        lessons = LessonOne.objects.filter(number=id).order_by('train_time')[0:5]
        list_lesson = [];
        for lesson in lessons:
            json_lesson = {'level1':str(lesson.level1),'level2':str(lesson.level2),'level3':str(lesson.level3),'level4':str(lesson.level4)
                               ,'level5':str(lesson.level5),'average':str(lesson.average),'date':lesson.train_time.strftime("%Y.%m.%d %H:%M")}
            list_lesson.append(json_lesson)
        return HttpResponse(json.dumps(list_lesson),content_type="application/json")
    elif str(lesson) == 'lesson2':
        lessons = LessonTwo.objects.filter(number=id).order_by('train_time')[0:5]
        list_lesson = [];
        for lesson in lessons:
            json_lesson = {'level1': str(lesson.level1), 'level2': str(lesson.level2), 'level3': str(lesson.level3),
                           'average': str(lesson.average),
                           'date': lesson.train_time.strftime("%Y.%m.%d %H:%M")}
            list_lesson.append(json_lesson)
        return HttpResponse(json.dumps(list_lesson), content_type="application/json")
    elif str(lesson) == 'lesson3':
        lessons = LessonThree.objects.filter(number=id).order_by('train_time')[0:5]
        list_lesson = [];
        for lesson in lessons:
            json_lesson = {'level1': str(lesson.level1), 'level2': str(lesson.level2), 'level3': str(lesson.level3),
                           'level4': str(lesson.level4), 'level5': str(lesson.level5)
                        , 'level6': str(lesson.level6), 'average': str(lesson.average),
                           'date': lesson.train_time.strftime("%Y.%m.%d %H:%M")}
            list_lesson.append(json_lesson)
        return HttpResponse(json.dumps(list_lesson), content_type="application/json")
    else:
        return HttpResponse("lesson is "+lesson+" and id is "+id)
#登录界面处理
def login(request):
    loginpost = LoginForm(request.POST);
    if loginpost.is_valid():
        return HttpResponseRedirect('/manage/people')
    else:
        # print loginpost.username
        return render(request,'manage/index.html',{'error':loginpost})

def reset_password(request):
    passwordpost = PasswordForm(request.POST)
    if passwordpost.is_valid():
        cleaned_data = passwordpost.clean()
        print cleaned_data
        user = SuperUser.objects.filter(username="admin",password=cleaned_data.get("origin"))[0]
        user.password = cleaned_data.get("password1")
        user.save()
        return render(request, 'manage/reset_password.html', {'succeed': 'succeed'})
    else:
        # print passwordpost.clean()
        return render(request, 'manage/reset_password.html', {'error': passwordpost})
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

