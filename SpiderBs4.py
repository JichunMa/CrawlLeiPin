from bs4 import BeautifulSoup

import JobOffers
import tools
from Spider import Spider


# Bs4爬取方式

class SpiderBs4(Spider):

    def __init__(self):
        Spider.__init__(self, 'bs4')

    def parse_job_list(self, data):
        job_offers_list = []
        soup = BeautifulSoup(data, 'html.parser')
        data_list = soup.select('ul.sojob-list li')
        index = 1
        for data in data_list:
            title = data.select('div.job-info h3 a')
            title = tools.safe_get_first_from_list(title)
            detail_url = title.attrs['href']

            title = tools.remove_all_whitespace(str(title.text))

            info_set = tools.safe_get_first_from_list(data.select('div.job-info p'))
            if info_set != "":
                info_set = info_set.attrs['title']
                salary, address, edu_request, experience = info_set.split('_')

            company_name = data.select('p.company-name a')
            company_name = tools.safe_get_first_from_list(company_name)
            if company_name != "":
                company_name = company_name.text
            business = tools.safe_get_first_from_list(data.select('a.industry-link'))
            if business != "":
                business = business.text
            job_offers = JobOffers.JobOffers(title, salary, address, edu_request, experience, company_name, business)
            job_description = self.request_job_detail(detail_url)
            job_offers.set_description(job_description)
            print('finished index ' + str(index) + ' / ' + str(len(data_list)))
            index = index + 1
            job_offers_list.append(job_offers)
        return job_offers_list

    def parse_job_detail(self, text):
        try:
            soup = BeautifulSoup(text, 'html.parser')
            detail_list = soup.find(name='div', attrs={"class": "content content-word"})
            result_detail = ''
            for detail in detail_list:
                result_detail = result_detail + str(detail)
                result_detail = result_detail.replace('<br/>', '')
            return result_detail
        except Exception as e:
            print(e)
            return ''
