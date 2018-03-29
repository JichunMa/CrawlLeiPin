import re

import JobOffers
import tools
from Spider import Spider


# Re爬取方式

class SpiderRe(Spider):

    def __init__(self):
        Spider.__init__(self, 're')

    def parse_job_list(self, source):
        rules = '<p class="condition clearfix"(.*?)>'
        data_list = re.findall(rules, source, re.S)
        salary_list = []
        address_list = []
        edu_request_list = []
        experience_list = []
        title_list = []
        company_name_list = []
        business_list = []
        job_description_list = []
        job_offers_list = []

        for data in data_list:
            data_set = tools.safe_get_first_from_list(re.findall('title="(.*?)"', data))
            salary, address, edu_request, experience = data_set.split('_')
            salary_list.append(salary)
            address_list.append(address)
            edu_request_list.append(edu_request)
            experience_list.append(experience)

        data_list = re.findall('<h3 title=".*?">(.*?)</h3>', source, re.S)
        index = 1
        for data in data_list:
            title = re.findall('<a .*?>(.*?)</a>', data, re.S)
            detail_url = re.findall('<a href="(.*?)".*?</a>', data, re.S)
            detail_url = tools.safe_get_first_from_list(detail_url)
            # 获取标题
            title = tools.safe_get_first_from_list(title)
            title = tools.remove_all_whitespace(title)
            title_list.append(title)

            # 获取工作描述
            job_description = self.request_job_detail(detail_url)
            job_description_list.append(job_description)
            print('finished index ' + str(index) + ' / ' + str(len(data_list)))
            index = index + 1

        # 获取公司名称
        data_list = re.findall('<p class="company-name">(.*?)</p>', source, re.S)
        for data in data_list:
            company_name_list_tmp = re.findall('<a .*?>(.*?)</a>', data, re.S)
            company_name = tools.safe_get_first_from_list(company_name_list_tmp)
            company_name_list.append(company_name)
        # 获取公司行业
        data_list = re.findall('<a class="industry-link" .*?>(.*?)</a>', source, re.S)
        for data in data_list:
            business_list.append(data)

        for i in range(len(title_list)):
            title = title_list[i]
            salary = salary_list[i]
            address = address_list[i]
            edu_request = edu_request_list[i]
            experience = experience_list[i]
            business = business_list[i]
            job_description = job_description_list[i]
            company_name = company_name_list[i]
            job_offers = JobOffers.JobOffers(title, salary, address, edu_request, experience, company_name, business)
            job_offers.set_description(job_description)

            job_offers_list.append(job_offers)
        return job_offers_list

    def parse_job_detail(self, text):
        try:
            rules = '<div class="content content-word">(.*?)</div>'
            data_list = re.findall(rules, text, re.S)
            if len(data_list) > 0:
                return data_list[0].replace('<br/>', '')
            else:
                return ''
        except Exception as e:
            print(e)
            return ''
