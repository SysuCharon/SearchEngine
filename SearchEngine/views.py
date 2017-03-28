#!/usr/bin/env python
# encoding:utf-8
"""
# Created Time :  下午2:25
# Author       : leo
# Filename     : views.py
# Desciption   :
"""

from __future__ import division
from django.views.generic import TemplateView
class index(TemplateView):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        error = True
        return self.render_to_response(self.get_context_data(error=error))

