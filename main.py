
from SpiderBs4 import SpiderBs4
from SpiderRe import SpiderRe
from SpiderXpath import SpiderXpath

if __name__ == '__main__':
    method = input('please choose a method:'
                   '\n 1.xpath'
                   '\n 2.re'
                   '\n 3.bs'
                   '\n')
    if method == '1':
        spider = SpiderXpath()
    elif method == '2':
        spider = SpiderRe()
    elif method == '3':
        spider = SpiderBs4()
    else:
        spider = SpiderXpath()

    spider.crawler_data()
