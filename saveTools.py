import xlwt


# 保存结果到xlsx
def output(filename, list_data):
    book = xlwt.Workbook()
    sh = book.add_sheet('sheet1')
    sh.write(0, 0, 'title')
    sh.write(0, 1, 'salary')
    sh.write(0, 2, 'address')
    sh.write(0, 3, 'edu_request')
    sh.write(0, 4, 'experience')
    sh.write(0, 5, 'company_name')
    sh.write(0, 6, 'business')
    sh.write(0, 7, 'job_description')
    column_index = 1
    for item in list_data:
        sh.write(column_index, 0, item.title)
        sh.write(column_index, 1, item.salary)
        sh.write(column_index, 2, item.address)
        sh.write(column_index, 3, item.edu_request)
        sh.write(column_index, 4, item.experience)
        sh.write(column_index, 5, item.company_name)
        sh.write(column_index, 6, item.business)
        sh.write(column_index, 7, item.job_description)
        column_index = column_index + 1
    book.save(filename)
