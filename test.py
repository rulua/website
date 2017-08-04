#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 17-8-4 上午11:25
# @Author  : ai-i-luru@interns.chuangxin.com

def application(env, start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return ["hello world"]