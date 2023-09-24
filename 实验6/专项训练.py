# 第一题
s1 = list(map(int, input().split()))
n = int(input())
if n not in s1:
    print('not found')
else:
    while n in s1:
        s1.remove(n)
    print(s1)
# 第二题
def IsFloatNum(str):
    s=str.split(',')
    if len(s)>2:
        return False
    else:
        for x in s:
            if not x.isdigit():
                return False
            return True


aList = list(eval(input()))
ls = []
for i in aList:
    if i.isdigit():
        i=int(i)
        ls.append(i)
    elif IsFloatNum(i):
        i=float(i)
        ls.append(i)
    else:
        ls.append(i)

print(ls)
# 第三题
from functools import reduce
aList = eval(input())
aList = [i for elem in aList for i in elem]
print(aList)
# 第四题
x=list()
count = 0
for i in range(1000,9000):
    a = int(i/1000)
    b = int(i%1000/1000)
    c = int(i%100/10)
    d = int(i%10)
    if a+b+c ==6 and a+c == b+d:
        x.append(i)
        count = count+1
print('符合的数字有',count,'个')
x.sort()
print(x)
# 第五题
ls = ['the lord of the rings','anaconda','legally’, blonde','gone with the wind']
n= (input())
if n=="1":
    print([i**3 for i in range(10)])
elif n=="2":
    print([i**3 for i in range(10) if not i %2])
elif n=="3":
    print([(i,i**3) for i in range (10) if i%2])
elif n=="4":
    print([i.title() for i in ls])
else:
    print("结束程序")
# 第六题
A = list(map(int, input().split()))
n = len(A)
new_List = [0] * n
listOdd = []
listEven = []

for num in A:
    if num % 2 == 0:
        listEven.append(num)
    else:
        listOdd.append(num)

if len(listOdd)!=len(listEven):
    print("ERROR")
else:
    A.sort()
    x=0
    for i in range(n):
        if A[i] %2==0:
            new_List[x] = A[i]
            x+=2

    y=1
    for j in range(n):
        if A[j]%2==1:
            new_List[y]=A[j]
            y+=2
    print(new_List)