# -*- coding: utf-8 -*-
import os
import tkinter as tk
import json
from tkinter import messagebox

import requests
import html


# 第1步，建立窗口window
window = tk.Tk()  # 建立窗口window

# 第2步，给窗口起名称
window.title('下载小红书图片')  # 窗口名称

# 第3步，设定窗口的大小(长＊宽)
window.geometry("240x240")  # 窗口大小(长＊宽)

# 第4步，在图形化界面上设定一个文本框
textExample = tk.Text(window, height=10)  # 创建文本输入框

# 第5步，安置文本框
textExample.pack()  # 把Text放在window上面，显示Text这个控件
result1 = ""




def fectchUrl(url):
    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'cookie': 'xhsTrackerId=1414db0f-940f-433b-8b4a-b64ba5fd99d6; '
                  'xhsTrackerId.sig=8I8N-ouWvfZzrAmIK3mNWa1MmxjMLa4j5n7n5799ZMU; xsecappid=xhs-pc-web; '
                  'a1=186b0fb4cf33qslwymeih1i3dko7v3nex04wdcmbi50000130577; webId=74ce2ced9b8ee56f261df42558013cf2; '
                  'web_session=030037a3370c9d5e5f7ba51e7c234afc2377ec; '
                  'gid=yYKD8iD2JKCJyYKD8iD4S8S6iqqAM1Ev6d3x4D3y3qfTlE28WhqIdf888yq82WW8JdWdyyyK; '
                  'gid.sign=oYD87SUpPsEEzR+ewW86xRdc0Ck=; abRequestId=74ce2ced9b8ee56f261df42558013cf2; '
                  'webBuild=3.8.1; cache_feeds=[]; '
                  'websectiga=3633fe24d49c7dd0eb923edc8205740f10fdb18b25d424d2a2322c6196d2a4ad; '
                  'sec_poison_id=6405b44e-4b0d-4e81-a6df-268f2c595590',
    }
    request = requests.get(url=url, headers=headers)
    return request.text


def parsing_lin(html):
    beginPos = html.find('imageList') + 11
    endPos = html.find('tagList"') - 2
    imageList = eval(html[beginPos: endPos])

    return imageList


def download(url, filename):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
    }
    with open(f'{filename}.jpg', 'wb+') as v:
        try:
            r = requests.get(url, headers= headers)
            v.write(r.content)
        except Exception as e:
            getTextInput()
            # messagebox.showinfo('提示', '下载失败！请重新点击下载')

            # print("下载失败")

# 第6步，获取文本框输入
def getTextInput():
    result = textExample.get("1.0", "end")  # 获取文本输入框的内容
    url = result
    # print(url)
    # print(result)  # 输出结果
    # print("输入小红书帖子的url:")
    try:
        html = fectchUrl(url)

        beginPos = html.find('imageList') + 11
        endPos = html.find('"tagList"') - 1
        imageList = eval(html[beginPos: endPos])
    except Exception as e:
        messagebox.showinfo('提示', '下载失败！')
    # print(imageList[0]['infoList'][1]['url'])
    for i in imageList:
        picUrl = i['infoList'][1]['url']
        # if os.path.exists("C:/xiaohongshu/"):
        fileId = picUrl[97:-21]
        download(picUrl, "C:/xiaohongshu/"+fileId[1:6])
        # os.mkdir(r'C:/xiaohongshu/')
    messagebox.showinfo('提示', '下载成功！')

# print("下载成功")



# Tkinter 文本框控件中第一个字符的位置是 1.0，可以用数字 1.0 或字符串"1.0"来表示。
# "end"表示它将读取直到文本框的结尾的输入。我们也可以在这里使用 tk.END 代替字符串"end"。


# 第7步，在图形化界面上设定一个button按钮（#command绑定获取文本框内容的方法）
btnRead = tk.Button(window, height=1, width=10, text="get", command=getTextInput)  # command绑定获取文本框内容的方法

# 第8步，安置按钮
btnRead.pack()  # 显示按钮

# 第9步，
window.mainloop()  # 显示窗口
