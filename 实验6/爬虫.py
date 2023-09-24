import os
from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import requests

# 图片链接
findImg = re.compile(r'<img.*src="(.*?)"/>')
# 图片名字
findName = re.compile(r'<img alt="(.*?)".*/>')





def getHtml(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43"

    }
    res = urllib.request.Request(url, headers=header)
    html = ''
    response = urllib.request.urlopen(res)
    html = response.read().decode("utf-8")
    return html


def getData(baseurl):
    datalist = []
    html = getHtml(baseurl)
    print(html)

    # 2.解析数据
    soup = BeautifulSoup(html, "html.parser")
    for i in soup.find_all('img'):
         # print(item)
        data = []
        i = str(i)
        # 图片名字
        name = re.findall(findName, i)
        data.append(name)
        # 图片链接
        img = re.findall(findImg, i)[0]
        data.append(img)

        datalist.append(data)

    return datalist


def saveData(datalist, savepath):
    global name, r
    print("save...")
    for i in range(0, 1600):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 2):
            if j == 0:
                name = str(data[j])
            else:
                r = requests.get('https://www.enterdesk.com/special/wmtp' + str(data[j]), stream=True)
        with open(savepath + name + '.jpg', 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)

def main():
    baseurl = "https://www.enterdesk.com/special/wmtp"
    datalist = getData(baseurl)
    path2 = r"E:\PY-Crawler"
    os.makedirs(path2 + './' + "img")
    savepath = path2 + './' + "img" + './'
    saveData(datalist, savepath)

if __name__ == "__main__":
    main()
