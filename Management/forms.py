#-*- coding: UTF-8 -*-
from django import forms
from models import *

class PersonForm(forms.Form):
    name = forms.CharField(required=True, error_messages={'required':'请填写您的真实姓名'})
    idcard = forms.CharField(required=True, error_messages={'required':'请填写您的身份证号码'})
    province = forms.CharField(required=True, error_messages={'required':'请填写您的籍贯'})
    age = forms.CharField(required=True, error_messages={'required':'请填写您的年龄'})
    phone = forms.CharField(required=True, error_messages={'required':'请填写您的电话号码'})
    email = forms.CharField(required=True, error_messages={'required':'请填写您的常用邮箱'})
    gender = forms.CharField(required=True, error_messages={'required':'请填写您的身份证性别'})
    address = forms.CharField(required=True, error_messages={'required':'请填写您的联系地址'})

class LoginForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required':'用户名不能为空'})
    password = forms.CharField(required=True, error_messages={'required':'密码不能为空'})
    def clean(self):
        cleaned_data = self.cleaned_data
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        count = SuperUser.objects.filter(username=username, password=password).count()
        if count == 0:
            raise forms.ValidationError('用户名或者密码错误')
        return cleaned_data

class PasswordForm(forms.Form):
    origin = forms.CharField(required=True, error_messages={'required':'请填写原始密码'})
    password1 = forms.CharField(required=True, error_messages={'required':'新密码不能为空'})
    password2 = forms.CharField(required=True, error_messages={'required': '请重新填写新密码'})
    def clean_origin(self):
        origin = self.cleaned_data.get("origin")
        count = SuperUser.objects.filter(username="admin", password=origin).count()
        if count == 0:
            raise forms.ValidationError('原始密码输入错误')
        return origin
    def clean_password2(self):
        cleaned_data = self.cleaned_data
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if str(password1) != str(password2):
            raise forms.ValidationError('两次填写密码不一致')
        return password2