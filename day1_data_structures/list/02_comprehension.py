squares_old = []
for x in range(10):
    squares_old.append(x ** 2)
print("传统写法：",squares_old)
 #列表推导（pythonic 写法）
squares_new = [x ** 2 for x in range(10)]
print("列表推导：",squares_new)


#-----基础形式---
nums = [1,2,3,4,5]
doubled = [x * 2 for x in nums]
squared = [x ** 2 for x in nums]
as_str = [str(x) for x in nums]

print("乘2:，", doubled)
print("平方：",squared)
print("转字符串：",as_str)

#---2 带过滤条件
numbers = range(20)

#只要偶数
evens = [x for x in numbers if x % 2 == 0]
print("偶数：",evens)

#只要大于10的
big = [x for x in numbers if x > 10]
print("大于10:",big)

#转换+过滤一起做：偶数的平方
even_squares = [x ** 2 for x in numbers if x % 2 == 0]
print("偶数的平方:",even_squares)

#---3.处理字符串列表
names = ["alice","bob","carol","dave"]

#全部转大写
upper_name = [name.upper() for name in names]
print("大写：",upper_name)

#只要长度大于3的
long_names = [name for name in names if len(name) > 3]
print("长度>3：",long_names)

#把每个名字变成“hello，xxx”
greetings = [f"Hello,{name.capitalize()}" for name in names]
print("打招呼：",greetings)

#---实战：处理接口返回的数据
#模拟一个接口返回的用户列表
users = [
    {"id":1,"name":"Alice","age":25,"status":"active"},
    {"id":2,"name":"bob","age":17,"status":"active"},
    {"id":3,"name":"Carol","age":"30","status":"inactive"},
    {"id":4,"name":"Dave","age":22,"status":"active"}

]

#提取所有用户的名字
all_names = [u["name"] for u in users]
print("所有用户名：",all_names)

#提取搜有active 用户的id
active_ids = [u["id"] for u in users if u["status"] == "active"]
print("成年 active 用户：",active_ids)

#成年且active 的用户名（多条件）
valid_names = [u["id"] for u in users if u["status"] == "active"]
print("active 用户的ID：",valid_names)

#------5嵌套循环---

#需求：生成3X3坐标对
pairs = [ (x,y) for x in range(3) for y in range(3)]
print("坐标对：",pairs)
 #带过滤：只要x！= y
diagonal_off =[(x,y) for x in range(3) for y in range(3) if x != y]
print("x !=y:",diagonal_off)
#----6三元表达式在推导里
#需求：正数保留，负数变0
numbers = [-3,1,-2,4,-5,6]
clipped = [x if x >0 else 0 for x in numbers]
print("正数保留，负数变0:",clipped)
