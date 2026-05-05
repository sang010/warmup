t1 = (1,2,3)
t2 = 1,2,3
empty = ()
print("t1:",t1)
print("t2:",t2)
print("empty:",empty)
single_correct = (1,)
not_a_tuple = (1)

print("singele_correct 的类型：",type(single_correct))
print("not_a_tuple的类型：",type(not_a_tuple))

#访问元素
colors = ("red","green","blue","yellow")

print(colors[0])
print(colors[-1])
print(colors[1:3])
print(len(colors))
print("red" in colors)

#   不能修改
nums = (1,2,3)

#4. 但可以重新赋值整个变量
nums = (1,2,3)
print("修改前 nums:",nums,"id:",id(nums))

nums = (4,5,6)
print("修改后nums:",nums,"id:",id(nums))

#5.tuple的查询方法
data = (1,2,3,2,1,2)
print("2出现次数：",data.count(2))
print("3的位置：",data.index(3))

#6.tuple也能做加法和乘法（生成新 tuple）
a = (1,2)
b = (3,4)

merged = a + b
repeated = a * 3

print("merged:",merged)
print("repeated:",repeated)

print("a 还是：",a)
print("b还是：",b)

#7.tuple和list互相转换
my_list = [1,2,3]
my_tuple = tuple(my_list)
my_tuple = tuple(my_list)
print("转 tuple:",my_tuple,type(my_tuple))

t = (1,2,3)
lst = list(t)
print("转 list:",lst,type(lst))