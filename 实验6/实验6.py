x = [i for i in range(1,5,1)]
print(x)
a = ['1','2','3','4']
#第一题
b = []
for i in a:
    for j in [x for x  in a if x!=i]:
        for m in [x for x in a if x!=i and x!=j]:
            b.append(int(i+j+m))
print(b)
print('互不相同且无重复数字的三位数总计 %s 个'%len(b))

#第二题
x1 = eval(input("请输入列表长度："))
x = []
print(x1)
for i in range(x1):
    x2 = eval(input("请输入元素："))
    x.append(x2)
print(x)
z = [0,1,2,3,4,5,False,'',None]
y = [False,None,0,'']
y2 = ["and","None"]
x = z
print(x)
for i in x:
    for j in y:
        if((i==j)):
            x.remove(i)
        for k in y2:
            if((str(i)==k)):
                x.remove(i)
print(x)

# 第三题
names = ['John', 'Amy', 'Jack']
scores = [98, 100, 85]  # 分数和名字是一一对应的
x = dict(zip(names,scores))
x2 = []
y= sorted(x2, reverse=True)
print(y)

#第四题
x = [52000.00,51000.00,48000.00]
y = [46800.00,45900.00,43200.00]
z = dict(zip(x,y))
z1 = []
for i in z.keys():
    z2 = i-z.get(i)
    z1.append(z2)
print(z1)


# 第五题

dic = {'admin':'123456','administrator':'12345678','root':'password'}

for j in range(3):
        x = input("请输入您的用户名：")
        y = input("请输入您的密码：")
        if x in dic.keys():
            if y in dic.values():
                print("登陆成功！")
                break
            else:
                print("登陆失败")


# 第6题
X = dict()
y = input()
List = y.split()
for i in List:
    if i in x:
        x[i] += 1
    else :
        x[i] = 1
print(x)

# 第七题
capitals = {'湖南':'长沙','湖北':'武汉','广东':'广州','广西':'南宁','河北':'石家庄','河南':'郑州','山东':'济南','山西':'太原','江苏':'南京','浙江':'杭州','江西':'南昌','黑龙江':'哈尔滨','新疆':'乌鲁木齐','云南':'昆明','贵州':'贵阳','福建':'福州','吉林':'长春','安徽':'合肥','四川':'成都','西藏':'拉萨','宁夏':'银川','辽宁':'沈阳','青海':'西宁','海南':'海口','甘肃':'兰州','陕西':'西安','内蒙古':'呼和浩特','台湾':'台北','北京':'北京','上海':'上海','天津':'天津','重庆':'重庆','香港':'香港','澳门':'澳门'}
while True:
    x = input()
    if x in capitals.values():
        print(capitals[x])
    elif x=="":
        break
    else:
        print("输入有错误")

# 第8题
a = int(input())
x = []

for i in range(a):
    j = input().split()

    dic = dict(name=j[0], age=int(j[1]))
    x.append(dic)

x.sort(key=lambda x: x['age'])
print(List)

x.sort(key=lambda x: x[' name '])
print(x)














