# 一.python基础知识
## 1.1.python变量
- python采用基于值的内存管理方式，不同变量赋相同值内存只保留一份，多个变量指向同一内存空间首地址
- [-5,256]内，这些变量共同用一个值的变量空间
- 变量类型
  -  --name私有变量
  -  --name-- 系统特殊成员变量
  -  -name 受保护成员
## 1.2.运算符表达式
- x//y 求整商 （分子分母中有小数，则计算结果保留小数）
- and or not 短路原则：前面满足条件则
- 求开方：math.sqrt()
- x与y的值交换：x,y = y,x
## 1.3.字符串
- split()字符串分割，字符串比较大小只比较第一个字符 即 289 34 ’34‘大
- 字符的索引:字符串有序，可通过索引（正向，负向）来获取索引元素正向：0，1，2 负向：-3，-2，-1
```python
name = 'tom'
print(name[-1])
print(name[0])
print(name[-2])
print(name[-3])
print(name[2]==name[-1])

#输出结果
#m
#t
#o
#t
#True
```
### 1.3.1.输出的几种方式
```python
a = 18
print(f'你好{a}')
print(f'你好{a:.2f}') #保留两位小数
print('你好'.format(a))
print('你好%d',a)
```
## 1.4.选择循环结构
- 双分支，双分支嵌套结构
### 1.4.1.双分支
- if ... not in 元组/列表
使用元组效率高于列表
```python
sex = input('请输入性别')
if (sex!='男'and sex!='女'): #其他语言写法
    print('输入错误')

if sex not in ('男','女'):#not in 元组/列表
    print('输入错误')

if sex  in ('男','女'):
    print('输入正确')
else:
    print('输入错误')
```
- print(a) if a > b else print(b) 为真返回前面为假后面
```python

# 输入男为0 否则为1
x = input('请输入性别')
print(0) if x == '男' else print(1)
```
- 输入两个值，比较a,b值的大小
```python
#输入两个值，比较a,b值的大小
a,b = input('请输入两个变量').split() #split()字符串分割，字符串比较大小只比较第一个字符 即 289 34 ’34‘大
if eval(a)>eval(b):
    print(a)
else:
    print(b)
# 使用map()函数
x = input('请输入两个变量')
a,b = map(int,x.split())#字符串分割之后转换int 然后赋给a,b
print(a) if a > b else print(b)
```
## 1.5.函数的定义
- 不需要指明形参类型
- 函数的调用
- 函数名小写
```python
score = input()
def fun(x):
      if x>10:
         return x
fun(score) 
```
### 输入分数案例
```python
score = eval(input('请输入分数'))
def func(score):
    degree = 'DCBAAE'
    if score >100 or score <0:
        print('输入错误')
    else:
        index = int((score - 60)//10)
        if index >= 0:
            return degree[index]
        else:
            return degree[-1]
print(func(score))
```
### 判断闰年案例
```python
x  = eval(input('请输入年份'))
print('闰年') if (x//400==0)|(x//4==0 and x//100!=0) else print('不是闰年')
```
for与while循环结构都有else可选子句
### for循环的列表推导式
```python
s = 0
for i in range(64):
    s = s+ 2**i
print(s)
#列表推导式[循环体 表达式]
a = sum([2**i for i range(64)])
```
### 通过循环遍历文件的内容 for line in file
### 文件的读取操作
- 1.打开文件 ----f.open(url,'r')返回一个文件对象 url=r'c:/text.text' (字符串之前加r保留原始字符串)
- 2.读文件，写文件-----f.read()读文件 f.write()写文件
- 3.关闭文件-------f.close()
### 枚举 enumerate() 返回一个可迭代对象（可通过循环遍历）
-  for i,v in enumerate(list,start=1开始元素): 用i,v保存索引和值
```python
list =['a','b','c']
for i,v in enumerate(list,start=1):
    print(i,v)
```

# 2.1.9列表推导式  过滤 
## (1).列表平铺
- [num for i in v for num in i]
```python
v = [[1,2,3],[2,5,8]]
print([num for i in v for num in i])
```
## (2).筛选 
- [i for i in range 列表 条件]
```python
a = [1,-3,5,6,-8,4,0]
# 筛选大于等于0的数
b = [i for i in a if i >=0]
# 过滤奇数
e = [i for i in a if i%2==0]
# 两倍输出
c = [i**2 for i in a]
print(b)
print(c)
```
## (3).os.listdir(r"路径")返回指定目录下的所有文件--列表
- .endswith(".doc"):  #判断后缀是否以.doc结尾
```python
# 找c盘下后缀为.doc的文件
import  os
for j in os.listdir(r"c:"):
    if j.endswith(".doc"):  #判断后缀
        print(j)
#  找c盘下后缀为.doc的文件-转列表推导式
[j for j in os.listdir(":c") if j.endswith(".doc")]
#判断是否是05结尾的
s = "245550205"
if s.endswith("05"):
    print("ok")
#判断是否是数字结尾的
```
# 2.3字典 
- 字典是无序，可变的
- 放在{}中 以键值对出现
```python
x = {}
x = dict()

```
## (1). zip()函数 （打包函数）把多个函数按照位置序列，将对应位置的元素打包在一起
- 返回zip对象
```python
a = ["a","b"]
b = [1,2]
c = list(zip(a,b))
print(c)
# 对应序列长度不一致，以短的为标准
e = [1,2,3]
c2 = list(zip(a,e))
print(c2)
c3 = dict(c2)
print(c3)
```
### 1.1.字典通过键找值
```python
a = {"name":"dog","sex":"man"}
print(a["name"])
```
### 1.2.字典通过键修改赋值
```python
a = {"name":"dog","sex":"man"}
a["name"] = "cat"
print(a["name"])
```
### 1.3.get()方法 获取键对应的值
```python
a = {"name":"dog","sex":"man","age":18}
print(a.get("age"))
print(a.get("age2")) #指定键不存在 返回none 不抛出异常
print(a.get("age2"),"不存在")# 返回不存在
```
### 1.4.items()方法 返回字典元素 for i in a.items()
```python
a = {"name":"dog","sex":"man","age":18}
for i in a.items():
    print(i)

```
### 1.5.keys()方法 返回键
```python
a = {"name":"dog","sex":"man","age":18}
for i in a.keys():
    print(i)
```
### 1.6.values()方法 返回值
```python
a = {"name":"dog","sex":"man","age":18}
for i in a.values():
    print(i)
```
### 1.7.添加元素
- 1.通过键添加
- 2.updata()----a.updata({键值对})
```python
# 1.通过键添加
a = {"name":"dog","sex":"man","age":18}
a["age"] = 19   #修改
a["age2"] = 20   #添加 
# 2.updata()
a.update({"age3":21})
print(a)
```
### 1.8.删除元素
- pop("键")
- popitem()---随机删除
- clear()---清空元素,保留字典对象
- del 字典名 ----删除字典对象
```python
a = {"name":"dog","sex":"man","age":18}
a.pop("age")
a.popitem() # 随机删除
a.clear()
print(a)
del a
print(a)
```
## (2).字典推导式
- {x:x.strip() for x in (' he ','she ',' i')}
- strip()----去除字符串两端的空格
- lstrip()-----去除字符串左边的空格
- rstrip()----去除字符串右边的空格
```python
# strip()----去除字符串两端的空格
s = " he"
new_s = s.strip()
print(s)
# 字典生成
y = ["A","B","C"]
x = ["a","b","c"]
z = {i:j for i,j in zip(x,y)}
print(z)
# 找出最高成绩
maxScore = max(z.values())
```
## 