from django.shortcuts import render, redirect, Http404
from django.template.response import TemplateResponse

from . import models
from album.models import Image


def home(request):
    return TemplateResponse(request, 'nogidb/home.html')

def member_list(request):
    members = models.Member.objects.all().order_by('status', 'birthday')
    return TemplateResponse(request, 'nogidb/member_list.html', {'members': members})

def condition(request, condition):
    if condition == 0:
        members = models.Member.objects.all().order_by('birthday')
    elif condition == 1:
        members = models.Member.objects.all().order_by('join_class', 'birthday')
    elif condition == 2:
        members = models.Member.objects.all().order_by('status', 'birthday')
    elif condition == 3:
        members = models.Member.objects.all().order_by('name_kana')
    else:
        return Http404
    return TemplateResponse(request, 'nogidb/member_list.html', {'members': members})

def member_detail(request, member_id):
    member = models.Member.objects.get(id=member_id)
    return TemplateResponse(request, 'nogidb/member_detail.html', {'member': member})


def grade(request):
    members = models.Member.objects.all().order_by('birthday')
    return TemplateResponse(request, 'nogidb/grade.html', {'members': members})


