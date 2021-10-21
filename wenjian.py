#读写文件
f = open(r"E:\python学习资料\python-\1.txt","r",encoding='utf-8')
content = f.read()
print(content)



with open(r"C:\Users\apple\Desktop\1.txt","r",encoding='utf-8') as file:
    for line in file:
        print(line)

#遍历字符串
for i in "nihhaoya":
    print(i)

#遍历列表 for item in ls:  for item in range(length(ls))

#枚举 enumerate() 返回一个可迭代对象（可通过循环遍历）
# for i,v in enumerate(list,start=1开始元素): 用i,v保存索引和值
list =['a','b','c']
for i,v in enumerate(list,start=1):
    print(i,v)

#else 子句 遇到break或者return语句结束程序或者遇到错误或者异常，则不会执行else语句
s = input()
for i in s:···
    if i not in '0123456789':
        break
else:
    print('所有字符串都是数字')

#for循环嵌套
X = 100
a = 5
b = 3
c = 1
# for i in
