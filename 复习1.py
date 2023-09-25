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
"""a2 = eval(input("请输入小数："))
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
        print(i)"""



"""
    4. list 列表
"""
"""# 除数字以外其他任何数值都必须要用单引号括起（无论是中文还是其他国家语言，都必须要），而数字数值可以不用单引号括起

# 4.1 列表创建的2种方式
# （1）list 创建
list1 = list() #创建空列表
list1 = list(('nihao',99,99.0)) #***** 注意：在使用 list() 函数创建列表时，一定要注意双括号。
print(list1)
list2 = list(map(eval,input("请输入数字用空格隔开来创建列表").split(" "))) # list 加上map创建
print(list2)

# （2）用[] 创建
list3 = ["jjj","哈哈哈",88,89.00]
print(list3)


# 4.2 list 的索引   #不包含切片右边的值
# （1）切片  [strat : end : step]   [strat : end]
print(list3[1:2])
print("从第一个开始每隔2个取一个：",list3[0:4:2])
# （2）下标索引
print(list3[0])
# (3)for循环遍历
# (4) 确定列表中是否存在指定的项 in 关键字   在就返回true 否则false
def one():
    if 88 in list3:
        return print("88在list3中")
    else:
        return print("88不在list3中")
one()

# 4.3 list 的合并和复制
# （1） +合并
one = ['你好',999]
one2 = list(('hh',66))
one3 = one+one2
print(one3)
# （2） 列表的复制 *
one4 = one*4
print(one4)

# 4.4 list 的嵌套
two = [['hh',88,00],'jj',[99,'pp']]
print(two)
print(two[0][1:3]) #不包含切片右边的值

# 4.5 列表比较需要引入 operator 模块的 eq 方法。

# 4.6 列表的函数
# （1） len() 判断长度
lit1 = list(('hhh',88,9090))
print(len(lit1))
# （2） type() 返回变量的类型
lit2 = list((88,3,4))
print(type(lit2))"""


# 5 集合
# 5，1 集合的创建
# （1） set()
list1 = list(('11',22,33))
set1 = set(list1)
print(set1)
set2 = {99,'hhh'}
print(set2)
# (2) {} 创建
set2 = {1,2,3,4}
set3 = set(range(1,9,3)) # range 创建的是[] 列表

print('set2为：',set2,'set3为：',set3)
# 5.2 集合的函数
#（1） update()方法更新整个元组
set2.update(set3)
print('set2为：',set2) # set2与set3并集

# (2) clear()方法用于清空整个集合
set2.clear()
print('set2为：',set2)

# (3) 通过discard()方法丢弃指定的元素
set3.discard(1)
print('set3为：',set3)

# (4) 通过remove()方法丢弃指定的元素
set3.discard(4)
print('set3为：',set3)

# (5) 通过pop()方法弹出最上面的元素 pop 弹出元素之后相当于删除元素
print('pop函数弹出set3元素：',set3.pop())
print('set3为：',set3)

# (6)集合增加元素  add()为末尾追加值 ； 通过updata 添加元素
set3.add(1) #末尾添加
print('set3为：',set3)

set3.update([1,3,5]) #并集
print('set3为：',set3)

# (7) 判断元素是否在集合中 in ; not in
print(8 in set3)
# （8） 删除整个集合 del; clear() 清除整个集合的元素
del set3
set2.clear()
print('set2为',set2)


# 5.3 集合的交集&、并集| 和差集- 数学运算
set2 = {1,4,6,9}
set3 = set(range(1,9,2))
print('set2为：',set2,'set3为：',set3)
print('set2与set3的交集为：',set2&set3)
print('set2与set3的并集为：',set2|set3)
print('set2与set3的差集为：',set2-set3)




# 6.




