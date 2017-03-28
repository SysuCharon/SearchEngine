# -*- coding: utf-8
# 备注：Military类中的military_information存储了新闻的信息，先start启动爬虫，再输出

import function
import time

craweler = function.Military()
print '请输入要查询的词语:',
Query_Word = raw_input()
print type(Query_Word)
print Query_Word
START_TIME = time.time()
craweler.start(Query_Word, multiprocess=True)
EXECUTE_TIME = time.time() - START_TIME
print 'Program Finished! Execute time is '+str(EXECUTE_TIME)+'s'
print '一共'+str(len(craweler.military_information))+'条记录，按下Enter打印'
raw_input()
for item in craweler.military_information:
    print '新闻标题:', item[0]
    print '发表部门:', item[1]
    print '发布时间:', item[2]
    print '新闻简介:', item[3]
    print '新闻网址:', item[4]
    print '\n'
