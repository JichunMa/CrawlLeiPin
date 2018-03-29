# coding:utf-8
import abc
import time

import networkTools
import saveTools


#
# 这是爬虫的抽象类，
# xpath,bs4,re 三种爬虫方式都继承这个类
# 因为所有的请求列表与详情是通用的，所以我这里把请求数据都放在基类中
# 然后调用爬取方式，爬取方式在子类中实现


class Spider(object):
    # 定义一个抽象类
    __metaclass__ = abc.ABCMeta
    crawl_type = ''

    def __init__(self, crawl_type):
        self.crawl_type = crawl_type

    # 抓去原始数据
    def crawler_data(self):
        for i in range(1, 2):
            url = "https://www.liepin.com/zhaopin/?ckid=e71acd4f94d5798f&fromSearchBtn=2&degradeFlag=0&" \
                  "init=-1&sfrom=click-pc_homepage-centre_searchbox-search_new&" \
                  "key=python&headckid=e71acd4f94d5798f&d_pageSize=40&" \
                  "siTag=I-7rQ0e90mv8a37po7dV3Q~fA9rXquZc5IkJpXC-Ycixw&d_headId" \
                  "=a4cff0646a5ef070a00f10d9b27ba3fd&d_ckId=a4cff0646a5ef070a00f10d9b27ba3fd&" \
                  "d_sfrom=search_fp&d_curPage=0&curPage={}".format(i)
            print('crawl url: ' + url)
            data_list = self.request_job_list(url)
            self.save_to_excel(data_list)
            # 采集不要太快了，否则容易造成ip被封或者网络请求失败
            time.sleep(2)

    def save_to_excel(self, data_list):
        print('suceess save file: ' + 'job_info_' + self.crawl_type + '.xlsx')
        saveTools.output('job_info_' + self.crawl_type + '.xlsx', data_list)

    # 获取工作列表
    def request_job_list(self, page_url):
        try:
            data = networkTools.request_via_network(page_url)
            if data != '':
                return self.parse_job_list(data)
        except Exception as e:
            print('\n\n出现错误,错误信息是:{}\n\n'.format(e))
            return ''

    # 解析工作列表的抽象类，具体实现在子类中
    @abc.abstractmethod
    def parse_job_list(self, text):
        pass

    # 获取工作详情
    # param job_href: 招聘工作的链接
    # return:
    def request_job_detail(self, job_href):
        try:
            print('获取详情地址 ' + job_href)
            data = networkTools.request_via_network(job_href)
            if data != '':
                return self.parse_job_detail(data)

        except Exception as e:
            print('\n\n出现错误,错误信息是:{}\n\n'.format(e))

    # 定义工作详情的抽象类
    @abc.abstractmethod
    def parse_job_detail(self, text):
        pass

