import jieba
import wordcloud
from matplotlib import pyplot as plt

txt = open("bg.txt", "r", encoding='gbk').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    elif word == "党中央" or word == "党":
        rword = "党中央"
    elif word == "习近平主席" or word == "习近平同志":
        rword = "习近平主席"
    elif word == "国家" or word == "我国":
        rword = "国家"
    else:
        rword = word
    counts[rword] = counts.get(rword,0) + 1
excludes = {"二人","不可","不能","如此"}
for word in excludes:
del counts[word]
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
print(items)
c = []
for i in range(50):
    word,count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
    c.append(word)
text = " ".join(c)
w = wordcloud.WordCloud(width=1000,font_path="msyh.ttc",mask=bg_pic,height=700)
w.generate(" ".join(jieba.lcut(txt)))
plt.imshow(w) #用词云图片
plt.axis('off') #不显示坐标
plt.show()
w.to_file("b4.jpg")