# 第一题
def taijie(x):
    x1 = 1
    x2 = 1
    count = 2
    if (x == 1):
        print("1")
    elif (x >= 2):
        while count < x:
            y = x1 + x2
            x1 = x2
            x2 = y
            count = count + 1
        print(y)


taijie(30)

# 第二题
import random
def f(prices):
    x = 0
    y = 0
    for i in range(len(prices)):
        if(i<(len(prices)-1)):
            if(prices[i]<prices[i+1]):
                y = prices[i]
                prices[i] = prices[i+1]
                x = x + prices[i] -y
        else:
            if(prices[i]<prices[-1]):
                y = prices[-1]
                x = prices[i]-y
    return x
n = random.randint(3,10)
ls = [random.randint(1,100) for i in range(0,n)]
print(ls)
print(f(ls))


# 第三题
def x():
    y = 1
    for i in range(9):
        y = 2 * (y + 1)
    print(y)


x()
# 第四题
import re


def f(m, n):
    # 定义函数体完成题目要求功能
    z = re.compile(r'[a-zA-Z]')
    z1 = z.findall(m)
    z2 = len(list(m))
    if (len(z1) == z2):
        n = list(n)
        m = list(m)
        m = sorted(set(m), key=m.index)
        # print(m)
        x = len(m)
        y = 0
        for i in m:
            for j in n:
                if (i == j):
                    y = y + 1
                    break
        # print(y,x)
        if ((y == x)):
            print("find")
        else:
            print("nofind")
    else:
        print("ERROR")


m, n = input("请输入两个字符串").split(" ")
# 完成该条件分支，输入字符串n判断单词m是否可以由n中的某些字符组成
f(m, n)



