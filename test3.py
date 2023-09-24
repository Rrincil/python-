import json
import requests
import html


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
        # try:
        r = requests.get(url, headers= headers)
        v.write(r.content)
        # except Exception as e:
        #     print("下载失败")


print("输入小红书帖子的url:")
url = input()
html = fectchUrl(url)
beginPos = html.find('imageList') + 11
endPos = html.find('"tagList"') - 1
imageList = eval(html[beginPos: endPos])
# print(imageList[0]['infoList'][1]['url'])
for i in imageList:
    picUrl = i['infoList'][1]['url']
    fileId = picUrl[97:-21]
    download(picUrl, "D:/test"+fileId)

print("下载成功")