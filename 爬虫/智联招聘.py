#/usr/bin/env python
#-*- coding:utf-8 -*-
import requests
import re
import xlwt
import xlrd
import xlutils
from xlutils.copy import copy

class Zl:
    def __init__(self,url_num):
        self.number = url_num
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'}
    def qingqiu(self):
        # url_1 = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=765&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.35008953&x-zp-page-request-id=9945055d3dda4f7382cedab4ed79496f-1541907459802-451727'.format(
        #     self.number)
        # url_1 = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=653&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.47431185&x-zp-page-request-id=b7f64a94563f469097ac690edaa0e33a-1542197607376-91460'.format(self.number)
        # url_1 = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=538&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.47431185&x-zp-page-request-id=b7f64a94563f469097ac690edaa0e33a-1542197607376-91460'.format(self.number)
        url_1 = 'https://fe-api.zhaopin.com/c/i/sou?start={}&pageSize=60&cityId=530&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88&kt=3&_v=0.73555295&x-zp-page-request-id=7c6818ea02454c36a059589b1e7a5593-1542197176286-209883'.format(self.number)
        response = requests.get(url=url_1,headers=self.head)
        html = response.content.decode('utf-8')
        patt = re.compile('jobType(.*?)rate')
        item_1 = patt.findall(html)
        return item_1

    def company(self):
        comp_list = []
        patt = re.compile('"url":(.*?)code')
        patt_1 = re.compile('"name":"(.*?)","size"')
        for i in self.qingqiu():
            item_2 = patt.findall(i)
            item_3 = patt_1.findall(item_2[0])
            comp_list.append(item_3[0])
        return comp_list

    def post(self):
        post_list = []
        patt = re.compile('"jobName":"(.*?)","industry"')
        for i in self.qingqiu():
            item = patt.findall(i)
            post_list.append(item[0])
        return post_list

    def Salary(self):
        Salary_list = []
        patt = re.compile('"salary":"(.*?)","emplType')
        for i in self.qingqiu():
            item = patt.findall(i)
            Salary_list.append(item[0])
        return Salary_list

    def EXP(self):
        exp_list = []
        patt = re.compile('"workingExp"(.*?)"eduLevel"')
        patt_1 = re.compile('"name":"(.*?)"},')
        for i in self.qingqiu():
            item = patt.findall(i)
            item_1 = patt_1.findall(item[0])
            exp_list.append(item_1[0])
        return exp_list

    def workplace(self):
        place = []
        patt = re.compile('city(.*?)},"applyType')
        patt_1 = re.compile('"display":"(.*?)"')
        for i in self.qingqiu():
            item = patt.findall(i)
            item_2 = patt_1.findall(item[0])
            place.append(item_2[0])
        return place

    def createDate(self):
        date = []
        patt = re.compile('"createDate":"(.*?)","endDate')
        for i in self.qingqiu():
            item = patt.findall(i)
            date.append(item[0])
        print(date)
        return date

    def people_url(self):
        url_number = []
        patt = re.compile('"positionURL":"(.*?)","workingExp')
        for i in self.qingqiu():
            item = patt.findall(i)
            url_number.append(item[0])
        return url_number

    def peo_num(self):
        num = []
        a = []
        for i in self.people_url():
            response = requests.get(url=i, headers=self.head)
            html = response.content.decode('utf-8')
            patt = re.compile('<span>招(.*?)人</span>')
            item = patt.findall(html)
            if item == a:
                num.append('0')
            else:
                num.append(item[0])
        return num

    def wp(self):
        place = []
        for i in self.people_url():
            response = requests.get(url=i, headers=self.head)
            html = response.content.decode('utf-8')
            patt = re.compile('class="icon-address"></span>(.*?)</p>')
            item = patt.findall(html)
            place.append(item)
        print(len(place))
        # return place
#
# zl = Zl(120)
# zl.createDate()
f = xlwt.Workbook(encoding='utf-8')
sheet = f.add_sheet('python_1')
f.save('智联招聘_北京.xls')
n = [0,60,120]
for i in n:
    zl = Zl(i)
    # zl.people_url()
    work_company = zl.company()
    work_place = zl.workplace()
    work_user = zl.peo_num()
    work_date = zl.createDate()
    work_jobname = zl.post()
    work_salary = zl.Salary()
    work_EXP = zl.EXP()

    lis_zhi = ('职位','公司名称','薪资','经验要求','招聘人数','工作地点','发布日期')
    # f = xlwt.Workbook(encoding='utf-8')
    f = xlrd.open_workbook('智联招聘_北京.xls')
    new_f = copy(f)
    sheet = new_f.add_sheet('北京{}'.format(i))
    for i in range(len(work_company)+1):
        if i == 0 :
            for k in range(7):
                sheet.write(i,k,lis_zhi[k])
        else:
            sheet.write(i,0,work_jobname[i-1])
            sheet.write(i,1,work_company[i-1])
            sheet.write(i,2,work_salary[i-1])
            sheet.write(i,3,work_EXP[i-1])
            sheet.write(i,4,work_user[i-1])
            sheet.write(i,5,work_place[i-1])
            sheet.write(i,6,work_date[i-1])
    new_f.save('智联招聘_北京.xls')
#





