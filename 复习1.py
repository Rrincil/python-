"""
    1. python 基于值的变量
"""
name1 = '你好'
name2 = '你好'
print('变量的地址：%d %d',id(name1),id(name2))
print("\n=================\n")

"""
    2. python 的输出方式
"""
# 2.1 %号模式
a1 = 18
a2 = 15.523
a3 = '你好呀就放假风'
a4 = '哈哈'
print("a1的值为：%d"%a1) #双引号”“ 加%
print("a1的值为：%d,a2的值为：%d"%(a1,a2)) #加%, 加括号\
# 2.2 format 格式
#format(输出项[,格式字符串]) , 其中格式字符串是可以选择项目
# {}内为输出内容格式 。format(变量集合)
# ''与format之间要加.即.format;   单个变量不用
print(format(a2,'.2f'))
print('{:.2f}'.format((a2))) #******    ‘’在左边的时候要加：
print('a1的值为：{},a2的值为：{:.2f},a3的值为：{}'.format(a1,a2,a3))
print('a3的值为：{0},a4的值为：{1}, {1},{0}'.format(a3,a4)) #字符串的映射

# print('a3的前三个值为：{0:2}'.format(a3))-------字符串的截取

# 2.3 f-string
# {变量名}
# 保留两位小数： {变量名: 保留格式}
# 字符串的截取： {str(变量名[])}切片
print(f'a1的值为{a1},a2的值为{a2:.2f},a3的值为{a3},a4的值为{str(a4[0])}')
print("\n=================\n")

# 2.4 混合输入
print("字符串加上数字：",a1,a2)

"""
    3. python 的输入方式
"""
#  3.1 是数字还是字符都将被作为字符串读取。如果想要接收数值，需要把接收到的字符串进行类型转换。例如，想要接收整型的数字并保存到变量num中
a1 = int(input('请输入数字：'))
print(f'a1的值为：{a1}')
print('a1的值为{}'.format(a1))
print("a1的值为: %d"%a1)

# 3.2 #eval()函数用来执行一个字符串表达式，并返回表达式的值。也可以用于返回数据本身的类型
# eval()函数
# 用来执行一个字符串表达式，并返回表达式的值。可以把字符串转化为list,dict ,tuple
a2 = eval(input("请输入小数："))
print("输出的是数字：%d"%a2)
a3 = input("请输入字符串：")
print(f'输出第一个字符：{a3[0]}')
print('输出字符{}'.format(a3))

# 3.3 多个输入
a,b = input("请输入两个字符串，以空格隔开").split(" ")
print(a+" "+b)
c,d = eval(input("请输入两个数字比较大小以逗号隔开")) # eval() arg 1 must be a string, bytes or code object
def bijiao():
    if c > d:
        return print(f'较大的值为{c}')
    else:
        return print(f'较大的值为{d}')
bijiao()
e,f,g = map(float,input("轻输入三个数字以空格隔开").split(" "))
print('e,f,g的值分别为{}  {}  {}'.format(e,f,g))

list1 = list(map(eval,input("请输入三个数字用空格隔开").split(" "))) #存入list列表
for i in list1:
    if i>0:
        print(i)

















