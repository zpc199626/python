#coding:utf-8
import requests
from bs4 import BeautifulSoup
import json

header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"}
payload = {"cate": "realtimehot"}
url = "https://s.weibo.com"
r = requests.get('http://s.weibo.com/top/summary?cate=realtimehot',data=payload,headers=header)

html = BeautifulSoup(r.text,'html.parser')
context2 = html.select(".td-02")
a = 1
new = []
links = []
for news in context2:
    title = news.select("a")[0].text
    # link = url + news.select("a")[0].get("href")
    link = str(url + "/weibo?q=%23" + title + "%23&Refer=top")
    new.append(title)
    links.append(link)
    a += 1


url = "https://oapi.dingtalk.com/robot/send?access_token=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"   #url为机器人的webhook
header = {
    "Content-Type": "application/json",
    "Charset": "UTF-8"
}
data = {
    "feedCard":{
        "links": [
            {"title":new[0],
             "messageURL":links[0]
            },
            {"title":new[1],
             "messageURL":links[1]
            },
            {"title":new[2],
             "messageURL":links[2]
            },
            {"title":new[3],
             "messageURL":links[3]
            },
            {"title":new[4],
             "messageURL":links[4]
            },
            {"title":new[5],
             "messageURL":links[5]
            },
            {"title":new[6],
             "messageURL":links[6]
            },
            {"title":new[7],
             "messageURL":links[7]
            },
            {"title":new[8],
             "messageURL":links[8]
            },
            {"title":new[9],
             "messageURL":links[9]
            },
            {"title":new[10],
             "messageURL":links[10]
            },
        ]
    },
    "msgtype": "feedCard",
}
sendData = json.dumps(data)
sendData = sendData.encode("utf-8")

request = requests.post(url=url, data=sendData, headers=header)

