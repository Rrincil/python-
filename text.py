# sex = input('请输入性别')
# if (sex!='男'and sex!='女'): #其他语言写法
#     print('输入错误')
#
# if sex not in ('男','女'):#not in 元组/列表
#     print('输入错误')
#
# if sex  in ('男','女'):
#     print('输入正确')
# else:
#     print('输入错误')
#
#输入两个值，比较a,b值的大小
# a,b = input('请输入两个变量').split() #split()字符串分割，字符串比较大小只比较第一个字符 即 289 34 ’34‘大
# if eval(a)>eval(b):
#     print(a)
# else:
#     print(b)
# # 使用map()函数
# x = input('请输入两个变量')
# a,b = map(int,x.split())#字符串分割之后转换int 然后赋给a,b
# if a>b:
#     print(a)
# else:
#     print(b)
#
# print(a) if a > b else print(b)
#
# # 输入男为0 否则为1
# x = input('请输入性别')
# print(0) if x == '男' else print(1)
#
# score  = input('请输入分数')
# map(int,score)

name = 'tom'
print(name[-1])
print(name[0])
print(name[-2])
print(name[-3])
print(name[2]==name[-1])

# score = eval(input('请输入分数'))
# def func(score):
#     degree = 'DCBAAE'
#     if score >100 or score <0:
#         print('输入错误')
#     else:
#         index = int((score - 60)//10)
#         if index >= 0:
#             return degree[index]
#         else:
#             return degree[-1]
# print(func(score))

x  = eval(input('请输入年份'))

print('闰年') if (x//400==0)|(x//4==0 and x//100!=0) else print('不是闰年')