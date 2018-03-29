class JobOffers:
    def __init__(self, title, salary, address, edu_request, experience, company_name, business, job_description=''):
        # title 招聘标题✓
        # salary 待遇 ✓
        # address 地区 ✓
        # edu_request 学历要求✓
        # experience 经验✓
        # company_name 公司名称✓
        # business 公司的行业✓
        # job_description 职位描述✓
        self.title = title
        self.salary = salary
        self.address = address
        self.edu_request = edu_request
        self.experience = experience
        self.company_name = company_name
        self.business = business
        self.job_description = job_description

    def set_description(self, description):
        self.job_description = description

    def display(self):
        print(self.title, self.salary, self.address, self.edu_request, self.experience, self.company_name,
              self.business, self.job_description)
