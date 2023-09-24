#列表使用
#https://blog.csdn.net/weixin_26737625/article/details/108494437?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164067061816780274139370%2522%252C%2522scm%2522%253A%252220140713.130102334..%2522%257D&request_id=164067061816780274139370&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~top_positive~default-1-108494437.first_rank_v2_pc_rank_v29&utm_term=%E5%88%97%E8%A1%A8%E8%BD%AC%E5%AD%97%E5%85%B8&spm=1018.2226.3001.4187

#https://python3-cookbook.readthedocs.io/zh_CN/latest/c01/p06_map_keys_to_multiple_values_in_dict.html
students=[{"id":"103","chinese":90,"math":85,"English":86},
{"id":"102","chinese":95,"math":98,"English":96},
{"id":"101","chinese":80,"math":81,"English":76}]
# 将students里面的数据提取出来放到字典scores中
# 按照学号从小到大输出各位同学的成绩
from collections import defaultdict
scores = defaultdict(list)
for j in students:
    #print(j.get("id"))
    scores[j.get('id')].append(j.get("chinese"))
    scores[j.get('id')].append(j.get("math"))
    scores[j.get('id')].append(j.get("English"))
#print(dict(scores))
y = dict(scores)
#print(y)
z = sorted(y.items(),key = lambda x :x[0])
z2 = sorted(y.keys())
for i in z:
    print(list(i)[0],"：",list(i)[1])
print(z)

s="it's a beautiful day. TOM's mom is my ant"
flag=0
t=s.count(" ")
for ch in s:
    if ch=="'":
        flag=flag+1
counts=t+1+flag
print(counts)

a = ["江苏",18,"北京",14]
b = ["浙江",15,"山东",55]
c = dict(zip(a,b))
print(c)



l1=[{1:'a',2:'b'},{3:'c',4:'d'}]
from collections import ChainMap
d3=ChainMap(*l1)
print (d3)#Output:ChainMap({1: 'a', 2: 'b'}, {3: 'c', 4: 'd'})
#Converting ChainMap object to dict using dict() constructor.
print (dict(d3))
#Output:{3: 'c', 4: 'd', 1: 'a', 2: 'b'}


print(list(zip([1,2], [3,4])))
a = (1,2,3)
print(a)



from collections import Counter
xia_dict={'江苏':3,'北京':2,'黑龙江':1,'广东':4}
di_dict={'江苏':8,'浙江':5,'山东':5,'安徽':4,'山西':2}
xia_dict,di_dict=Counter(xia_dict),Counter(di_dict)
print(xia_dict)
xia_dict=dict(xia_dict+di_dict)
print(xia_dict)





students= [
    {'id':'103','Chinese': 90,'Math':85,'English':86},
    {'id':'102','Chinese': 95,'Math':98,'English':96},
    {'id':'101','Chinese': 80,'Math':81,'English':76}
]

scores = {}
for student in students:
    sv = student.items()
    v = []
    for it in sv:
        if it[0] =='id':
            k = it[1]
        else:
            v.append(it[1])
    scores[k]  = v
print(scores)

# so = list(scores.items())
# so.sort(key = lambda x:x[0],reverse = False)
# for l in so:
#     print('{}:{}'.format(l[0],l[1]))


x = {1,1,2}

print(x)




res = 0
for i in range(1, 306):
    a = list(str(i))
    res += a.count('5')
print(res)

x = "hdjd"
y =sorted(x,reverse = True)
print(len(list(x)))



import random
random.seed(0)
x = ["hhd","hjjj"]
name = x[random in range(0,5)]
print(name)