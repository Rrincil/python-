#一.python基础知识
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