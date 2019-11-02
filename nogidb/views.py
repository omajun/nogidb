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
    age = member.age() 
    return TemplateResponse(request, 'nogidb/member_detail.html', {'member': member, 'age':age})


def grade(request):
    members_1990 = models.Member.objects.filter(birthday__range=["1990-04-02", "1991-04-01"]).order_by('birthday')
    members_1991 = models.Member.objects.filter(birthday__range=["1991-04-02", "1992-04-01"]).order_by('birthday')
    members_1992 = models.Member.objects.filter(birthday__range=["1992-04-02", "1993-04-01"]).order_by('birthday')
    members_1993 = models.Member.objects.filter(birthday__range=["1993-04-02", "1994-04-01"]).order_by('birthday')
    members_1994 = models.Member.objects.filter(birthday__range=["1994-04-02", "1995-04-01"]).order_by('birthday')
    members_1995 = models.Member.objects.filter(birthday__range=["1995-04-02", "1996-04-01"]).order_by('birthday')
    members_1996 = models.Member.objects.filter(birthday__range=["1996-04-02", "1997-04-01"]).order_by('birthday')
    members_1997 = models.Member.objects.filter(birthday__range=["1997-04-02", "1998-04-01"]).order_by('birthday')
    members_1998 = models.Member.objects.filter(birthday__range=["1998-04-02", "1999-04-01"]).order_by('birthday')
    members_1999 = models.Member.objects.filter(birthday__range=["1999-04-02", "2000-04-01"]).order_by('birthday')
    members_2000 = models.Member.objects.filter(birthday__range=["2000-04-02", "2001-04-01"]).order_by('birthday')
    members_2001 = models.Member.objects.filter(birthday__range=["2001-04-02", "2002-04-01"]).order_by('birthday')
    members_2002 = models.Member.objects.filter(birthday__range=["2002-04-02", "2003-04-01"]).order_by('birthday')
    members_2003 = models.Member.objects.filter(birthday__range=["2003-04-02", "2004-04-01"]).order_by('birthday')
    members_2004 = models.Member.objects.filter(birthday__range=["2004-04-02", "2005-04-01"]).order_by('birthday')

    return TemplateResponse(
        request,
        'nogidb/grade.html',
        {
        'members_1990': members_1990,
        'members_1991': members_1991,
        'members_1992': members_1992,
        'members_1993': members_1993,
        'members_1994': members_1994,
        'members_1995': members_1995,
        'members_1996': members_1996,
        'members_1997': members_1997,
        'members_1998': members_1998,
        'members_1999': members_1999,
        'members_2000': members_2000,
        'members_2001': members_2001,
        'members_2002': members_2002,
        'members_2003': members_2003,
        'members_2004': members_2004,
        }
        )

def grade_condition(request, status):
    if status == 0:
        members = models.Member.objects.filter(status=0).order_by('birthday')
        members_1990 = members.filter(birthday__range=["1990-04-02", "1991-04-01"]).order_by('birthday')
        members_1991 = members.filter(birthday__range=["1991-04-02", "1992-04-01"]).order_by('birthday')
        members_1992 = members.filter(birthday__range=["1992-04-02", "1993-04-01"]).order_by('birthday')
        members_1993 = members.filter(birthday__range=["1993-04-02", "1994-04-01"]).order_by('birthday')
        members_1994 = members.filter(birthday__range=["1994-04-02", "1995-04-01"]).order_by('birthday')
        members_1995 = members.filter(birthday__range=["1995-04-02", "1996-04-01"]).order_by('birthday')
        members_1996 = members.filter(birthday__range=["1996-04-02", "1997-04-01"]).order_by('birthday')
        members_1997 = members.filter(birthday__range=["1997-04-02", "1998-04-01"]).order_by('birthday')
        members_1998 = members.filter(birthday__range=["1998-04-02", "1999-04-01"]).order_by('birthday')
        members_1999 = members.filter(birthday__range=["1999-04-02", "2000-04-01"]).order_by('birthday')
        members_2000 = members.filter(birthday__range=["2000-04-02", "2001-04-01"]).order_by('birthday')
        members_2001 = members.filter(birthday__range=["2001-04-02", "2002-04-01"]).order_by('birthday')
        members_2002 = members.filter(birthday__range=["2002-04-02", "2003-04-01"]).order_by('birthday')
        members_2003 = members.filter(birthday__range=["2003-04-02", "2004-04-01"]).order_by('birthday')
        members_2004 = members.filter(birthday__range=["2004-04-02", "2005-04-01"]).order_by('birthday')

    elif status == 1:
        members = models.Member.objects.filter(status=1).order_by('birthday')
        members_1990 = members.filter(birthday__range=["1990-04-02", "1991-04-01"]).order_by('birthday')
        members_1991 = members.filter(birthday__range=["1991-04-02", "1992-04-01"]).order_by('birthday')
        members_1992 = members.filter(birthday__range=["1992-04-02", "1993-04-01"]).order_by('birthday')
        members_1993 = members.filter(birthday__range=["1993-04-02", "1994-04-01"]).order_by('birthday')
        members_1994 = members.filter(birthday__range=["1994-04-02", "1995-04-01"]).order_by('birthday')
        members_1995 = members.filter(birthday__range=["1995-04-02", "1996-04-01"]).order_by('birthday')
        members_1996 = members.filter(birthday__range=["1996-04-02", "1997-04-01"]).order_by('birthday')
        members_1997 = members.filter(birthday__range=["1997-04-02", "1998-04-01"]).order_by('birthday')
        members_1998 = members.filter(birthday__range=["1998-04-02", "1999-04-01"]).order_by('birthday')
        members_1999 = members.filter(birthday__range=["1999-04-02", "2000-04-01"]).order_by('birthday')
        members_2000 = members.filter(birthday__range=["2000-04-02", "2001-04-01"]).order_by('birthday')
        members_2001 = members.filter(birthday__range=["2001-04-02", "2002-04-01"]).order_by('birthday')
        members_2002 = members.filter(birthday__range=["2002-04-02", "2003-04-01"]).order_by('birthday')
        members_2003 = members.filter(birthday__range=["2003-04-02", "2004-04-01"]).order_by('birthday')
        members_2004 = members.filter(birthday__range=["2004-04-02", "2005-04-01"]).order_by('birthday')

    
    return TemplateResponse(request, 'nogidb/grade.html',
    {
        'members_1990': members_1990,
        'members_1991': members_1991,
        'members_1992': members_1992,
        'members_1993': members_1993,
        'members_1994': members_1994,
        'members_1995': members_1995,
        'members_1996': members_1996,
        'members_1997': members_1997,
        'members_1998': members_1998,
        'members_1999': members_1999,
        'members_2000': members_2000,
        'members_2001': members_2001,
        'members_2002': members_2002,
        'members_2003': members_2003,
        'members_2004': members_2004,
        })



