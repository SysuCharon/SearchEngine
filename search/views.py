#!/usr/bin/env python
# encoding:utf-8
"""
# Created Time :  下午3:32
# Author       : leo
# Filename     : views.py
# Desciption   :
"""

from __future__ import division
from django.views.generic import TemplateView

import function
import time

class search(TemplateView):
    template_name = "search_result.html"

    def get(self, request, *args, **kwargs):
        ListInfo = ['title', 'dep', 'time', 'abst', 'site']
        key = request.GET['keyword'].encode('utf-8')
        cur_page = int(request.GET['page'])
        is_search = int(request.GET['isSearch'])

        record_start = cur_page * 10 - 10
        record_end = cur_page * 10
        if cur_page <= 8:
            pages = range(1, 11)
        else:
            pages = range(cur_page - 7, cur_page + 3)

        page = {"pages": pages, "cur_page": cur_page, "record_start": record_start, "record_end":record_end, "pre": cur_page - 1, "next":cur_page + 1}

        print "type(key)", type(key)
        print 'key:' , key
        craweler = function.Military()
        START_TIME = time.time()
        craweler.start(key, multiprocess=True)

        EXECUTE_TIME = time.time() - START_TIME
        result = craweler.military_information
        #sort
        docs = sorted(result, key=lambda x:x[2], reverse=True)
        for index,doc in enumerate(docs):
            docs[index] = dict(zip(ListInfo, doc))
        print "end sort"
        error = False

        if len(docs)==0: error=True
        return self.render_to_response(self.get_context_data(key=key,
                                                             error=error,
                                                             time=round(EXECUTE_TIME,5)+0.00001,
                                                             num = len(docs),
                                                             docs=docs,
                                                             page=page))
