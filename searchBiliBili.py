# -*- coding:utf-8 -*-
import requests
import datetime
import bs4
import time

def openUrl(url):
    headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.49"} 
    result = requests.get(url=url,headers=headers)
    return result


def getHtml(keyword):
    url = "https://search.bilibili.com/all?keyword={}&order=pubdate&duration=0&tids_1=0".format(keyword)
    result = openUrl(url)
    soup = bs4.BeautifulSoup(result.text,"html.parser")
    target = soup.find("span",title="上传时间")
    return target.text.strip()

def hasNew(keyword):
    date = getHtml(keyword)
    today = datetime.date.today()
    if date == today.strftime("%Y-%m-%d"):
        print("有新稿件")
        print("最新投稿日期：",date)
        print("今天是：",datetime.date.today())
    else:
        print("没有新稿件")
        print("最新投稿日期：",date)
        print("今天是：",datetime.date.today())



def main():
    while True:
        keyword = input("输入：")
        if keyword == "":
            keyword = "f900xr"
        hasNew(keyword)
        time.sleep(1)
if __name__ == "__main__":
    main()