#2.1.9列表推导式  过滤 [i for i in range 列表 条件]
## 筛选
a = [1,-3,5,6,-8,4,0]
# 筛选大于等于0的数
b = [i for i in a if i >=0]
# 过滤奇数
e = [i for i in a if i%2==0]
# 两倍输出
c = [i**2 for i in a]
print(b)
print(c)
v = [[1,2,3],[2,5,8]]
print(num for i in v for num in i)
import  os


s = "245550205"
if s.endswith("05"):
    print("ok")

y = ["A","B","C"]
x = ["1","53","99"]
z = {i:j for i,j in zip(y,x)}
z3 =[]
for i in z.values():
    int(i)
    z3.append(int(i))
z4 = z3.sort()
print(z3)

