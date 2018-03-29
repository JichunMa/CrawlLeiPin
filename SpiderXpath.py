from lxml import etree

import JobOffers
import tools
from Spider import Spider


# Xpath爬取方式

class SpiderXpath(Spider):
    def __init__(self):
        Spider.__init__(self, 'xpath')

    def parse_job_list(self, data):
        source = etree.HTML(data)
        list_item = source.xpath('//div[@class="sojob-item-main clearfix"]')
        job_offers_list = []
        index = 1
        for item in list_item:
            item_job_info = tools.safe_get_first_from_list(item.xpath('div[@class="job-info"]'))
            company_info = tools.safe_get_first_from_list(item.xpath('div[@class="company-info nohover"]'))
            # 数据来自 item_job_info
            title = tools.safe_get_first_from_list(item_job_info.xpath('h3/a/text()'))
            title = tools.remove_all_whitespace(title)
            salary = tools.safe_get_first_from_list(item_job_info.xpath('p/span[@class="text-warning"]/text()'))
            address = tools.safe_get_first_from_list(item_job_info.xpath('p/a/text()'))
            detail_link = tools.safe_get_first_from_list(item_job_info.xpath('h3/a/@href'))
            edu_request = tools.safe_get_first_from_list(item_job_info.xpath('p/span[@class="edu"]/text()'))
            experience = tools.safe_get_first_from_list(item_job_info.xpath('p/span[3]/text()'))
            # 数据来自 company_info
            company_name = tools.safe_get_first_from_list(company_info.xpath('p/a/text()'))
            business = tools.safe_get_first_from_list(company_info.xpath('p[@class="field-financing"]/span/a/text()'))
            job_offers = JobOffers.JobOffers(title, salary, address, edu_request, experience, company_name, business)
            job_description = self.request_job_detail(detail_link)
            job_description = tools.remove_all_whitespace(job_description)
            job_offers.set_description(job_description)
            job_offers_list.append(job_offers)
            print('finished index ' + str(index) + ' / ' + str(len(list_item)))
            index = index + 1
        return job_offers_list

    def parse_job_detail(self, text):
        try:
            source = etree.HTML(text)
            detail = source.xpath('//div[@class="content content-word"]')
            if len(detail) > 0:
                detail = detail[0]
                detail = detail.xpath('string(.)')
                return detail
            else:
                return ''
        except Exception as e:
            print(e)
        return ''
