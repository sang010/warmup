nums = [1,2,3]
empty = []
from_range = list(range(10))
repeated = [0] * 5
 
print("nums:",nums)
print("from_range:",from_range)
print("repeated:",repeated)



# -----2.访问元素 -----
fruits = ["apple","banana","cherry","date"]

print(fruits[0])
print(fruits[-1])
print(fruits[1:3])
print(fruits[:2])
print(fruits[2:])
print(fruits[::-1])

# -----3.修改列表
colors = ["red","green"]

colors.append("blue")
colors.insert(0,"black")
colors.extend(["white","gray"])
print("after append/insert/extend:",colors)

a = [1,2]
a.append([3,4])
print("extend 整个列表：",a)

b = [1,2]
b.extend([3,4])
print("extend 整个列表：",b)

#---4.删除元素

takes = ["写代码","开会","吃饭","写代码","睡觉"]

takes.remove("写代码")
print("remove 后",takes)

last = takes.pop()
print("pop返回的：",last,"剩余：",takes)

first = takes.pop(0)
print("pop(0)返回的",first,"剩余",takes)

#---5.查询相关
grades = [85,90,75,90,60]

print("长度：",len(grades))
print("最大：",max(grades))
print("最小",min(grades))
print("求和：",sum(grades))
print("90在吗：",90 in grades)
print("90首次位置",grades.index(90))
print("90出现次数：",grades.count(90))

#----排序

numbers = [3,1,4,1,5,9,2,6]
asc = sorted(numbers)
desc = sorted(numbers,reverse = True)
print("原列表：",numbers)

words = ["banana","apple","cherry"]
words.sort(key=len)
print("按长度排序：",words)

students = [
    {"name":"Alice","age":25},
    {"name":"Bob","age":20},
    {"name":"Carol","age":30}
] 
students.sort(key=lambda s: s["age"])
print("按年龄排序：",students)



