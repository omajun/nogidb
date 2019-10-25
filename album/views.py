from django.shortcuts import render
from django.template.response import TemplateResponse
from .models import Image
from nogidb.models import Member


def member_detail(request, member_id):
    member = Member.objects.get(id=member_id)
    images = Image.objects.filter(name=member)
    return TemplateResponse(request, 'album/member_detail.html', {'images': images, 'member': member})
