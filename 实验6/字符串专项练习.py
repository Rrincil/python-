# 第一题
## （1）字符串中所有英文字符转为大写输出
s = "nihao"
print(s.upper())
## （2）转小写
s = "JKDF"
print(s.lower())
## （3）分割字符串
s = input("请输入字符串：").split()
print(s)
## (4) 列表转字符串 join连接
t = ["s","c","h","o","o","l"]
print(" ".join(t))
## （5）列表转字符串  字符“-”连接后输出
print("-".join(t))
## （6） 用'/'连接后输出
print("/".join(t))
## （7）存在字符 返回位置
s = "do you the pig"
s1 = "the"
if s1 in s:
    print(s.find(s1))
## (8)替换
r = s.replace("the","a")
print(r)
# 第二题
import string
def check():
    ch = input("请输入字符串：")
    r = [False]*4
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    for i in ch:
        if i.islower():
            m1 = m1+1
        elif i.isupper():
            m2 = m2 + 1
        elif i.isdigit():
            m3 = m3 + 1
        elif i == ' ':
            m4 = m4 + 1
        else:
            m5 = m5 + 1
    print(m1,m2,m3,m4,m5)
check()
# 第三题
x = input("请输入ip地址：").split(".")
t = 0
for i in x:
    if i.isdigit():
        i = int(i)
        if i>0&i<255:
            t = t+1
    else:
        print("No")
if t==4:
    print("Yes")
# 第四题
b = int(input("在第几个位置分隔："))
a = "python语言程序设计"
c=a[b-1:b]
d=a.split(c)
print(d[0])
print(d[1])

# 第五题
a=input("请输入:")
b,c,d,e,f=0,0,0,0,0
if len(a)>=8:
    f=1
for i in a:
    if i.islower():
        b=1
    elif i.isupper():
        c=1
    elif i.isdigit():
        d=1
    else :
        e=1
h=b+c+d+e
if f==0:
    print("弱密码")
if f==1 and h==1:
    print("弱密码")
if f==1 and h==2:
    print("中等密码")
if f==1 and h==3:
    print("强密码")
if f==1 and h==4:
    print("极强密码")


# 第六题
a=input("请输入:")
c=''.maketrans('qwert','abcde')
print(a.translate(c))
# 第七题
d=int(input("请输入同学个数:"))
a=[]
b=[]
c=[]
for i in range(d):
    t=str(input("请输入学号:"))
    a.append(t)
    t=str(input("请输入姓名:"))
    b.append(t)
    t=str(input("请输入手机号:"))
    c.append(t)
for i in range(d):
    c1=a[i]
    print(c1.replace(c1[3:8],"*****"))
    c1=b[i]
    print(c1.replace(c1[1:3],"*"))
    c1=c[i]
    print(c1.replace(c1[3:8],"*****"))
# 第八题
a=str(input("请输入:"))
b=len(a)
if b%2==0:
     c1=a[0:int(b/2)]
     c2=a[int(b/2):b]
     c2=c2[::-1]
     if c1==c2:
         print("是回文")
     else:
         print("不是")
else:
     c1=a[0:int(b/2)+1]
     c2=a[int(b/2):b]
     c2=c2[::-1]
     if c1==c2:
         print("是回文")
     else:
         print("不是")
# 第九题
x = input("请输入学生信息：").split()

print("姓名：",x[1])
print("班级：",x[2],x[3])
print("出生：",x[5])