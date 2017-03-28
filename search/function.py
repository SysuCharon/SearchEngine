# -*-coding:utf-8 -*-
# Author:   林东定
# Function: 爬取'百度新闻的内容', 返回list
import urllib2
import urllib
from bs4 import BeautifulSoup
import re
import threading


# 抓取百度新闻消息
class Military:
    # 初始化方法，定义变量
    def __init__(self):
        self.military_information = []

    # 获取页面
    @staticmethod
    def get_page(self, query_word):
        try:
            word = urllib.quote(query_word)
            url = 'http://news.baidu.com/ns?cl=2&rn=40&tn=news&word='+word+'&pn=0'
            user_agent = 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36'
            headers = {'User-Agent': user_agent}
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            page_code = response.read().decode('utf-8')
            return urllib.unquote(page_code)
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason
            return

    # 解析页面
    def analysis_page(self, query_word, lock=None):
        this_page_information = []
        now_href = []
        page_code = self.get_page(self, query_word)
        if not page_code:
            print "The Page Lode Failed"
            return None
        # 用BeautifulSoup对网页进行解析
        soup = BeautifulSoup(page_code, "html.parser")
        for item in soup.find_all(class_='result'):
            infor = []
            href = item.find_all('a')[0]
            if not href.get('href') in now_href:
                now_href.append(href.get('href'))
            else:
                continue
            site_and_time = item.find_all(class_='c-author')[0].get_text().split()
            site_ = site_and_time[0]
            time_ = ""
            for timei in site_and_time[1:]:
                time_ = time_ + timei.strip()
            line = str(item.find_all('div')[0])
            s = r".*?</p>(.*?)<span"
            result = re.findall(s, line)[0]
            re_tag = re.compile('</?\w+[^>]*>')
            result = re_tag.sub('', result).strip()
            infor.append(href.get_text())
            infor.append(site_)
            infor.append(time_)
            infor.append(result)
            infor.append(href.get('href'))
            this_page_information.append(infor)
        if lock is not None:
            lock.acquire()
            self.military_information.extend(this_page_information)
            lock.release()
        else:
            self.military_information.extend(this_page_information)

    # 程序开始执行
    def start(self, query_word, multiprocess=False):
        sites = ['www.mod.gov.cn', 'www.miit.gov.cn', 'www.sastind.gov.cn', 'www.caea.gov.cn', 'www.weain.mil.cn', 'www.cetin.net.cn', 'www.dsti.net', 'www.comac.cc']
        if multiprocess is True:
            # 多线程
            threads = []
            mylock = threading.RLock()
            for site in sites:
                t = threading.Thread(target=self.analysis_page, args=(query_word+' site:'+site, mylock))
                t.setDaemon(True)
                threads.append(t)
            for t in threads:
                t.start()
            for t in threads:
                t.join()
        else:
            # 单线程
            for site in sites:
                self.analysis_page(query_word + ' site:' + site)
