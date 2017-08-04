# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.template import loader
import os
def index(request):
    template = loader.get_template('adsapp/index.html')
    context={}
    return HttpResponse(template.render(context,request))

#@csrf_protect
def upload(request):
    if request.method == 'POST':
        email = request.POST['email']
        imagefile=request.FILES.get('imagefile',None)
        destination= open(os.path.join("/home/luru/Desktop/ads/adsapp/upload/",imagefile.name),'wb+')
        destination.write(imagefile.read())
        template = loader.get_template('adsapp/success.html')
        context={}
        context['email']=email
        return HttpResponse(template.render(context,request))
    else:
        return HttpResponse('error')
def tt(request):
    template = loader.get_template('adsapp/t.html')
    context = {}
    return HttpResponse(template.render(context, request))

