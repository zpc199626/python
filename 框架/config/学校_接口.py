#！/usr/bin/env python
# -*- coding: utf-8 -*-
import requests

class school_查询():

    def school_快查(self,a):
        url = "http://testsupport-be.haofenshu.com/v1/schools/infos"
        canshu = {"filterInput": "{}".format(a)}
        header = {'Content-Type': 'application/x-www-form-urlencoded',
                  'Accept': '*/*',
                  'Accept-Encoding': 'gzip, deflate, br',
                  'Accept-Language': 'zh-CN,zh;q=0.9',
                  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
                  'Cookie': 'yz-test-session-id=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJvcGVyYXRvciI6ImxpeGlhbndlaSIsInJvbGVUeXBlIjoxLCJpYXQiOjE1MzkwNTgxOTYsImV4cCI6MTU3MDU5NDE5Nn0.GzWTsN7Sb9W85R1Wem8_HNV7e8oXTQSCPdvODb5f_GA'}
        res = requests.post(url=url, headers=header, params=canshu)
        html = res.json()
        return html


