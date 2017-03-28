#!/usr/bin/env python
# encoding:utf-8
"""
# Created Time :  下午3:29
# Author       : leo
# Filename     : urls.py
# Desciption   :
"""
from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', search.as_view()),
]