#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-7-18 上午11:07
# @Author  : ai-i-luru@interns.chuangxin.com
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^upload/$',views.upload,name='upload'),
    url(r'^tt/$',views.tt,name='tt'),
]