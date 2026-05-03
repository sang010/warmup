#---坑位---
print("--【坑1】赋值 不等于 复制---")
 
a = [1,2,3]
b = a
b.append(4)

print("a",a)
print("b",b)

#---验证：它们确实是同一个对象---
print("\n---【证据】a和b是同一个对象---")

print("a的id：",id(a))
print("b的id：",id(b))
print("a is b:",a is b)
print("a == b")

#正确做法：用.copy()或切片
print("\n---【解决】真正的复制---")
original = [1,2,3]

copied1 = original.copy()
copied2 = original[:]
copied3 = list(original)

copied1.append(99)
copied2.append(100)
copied3.append(101)

print("original:",original)
print("copied1:",copied1)
print("copied2:",copied2)
print("copied3:",copied3)

#三种肤质方法人选，日常最常用.copy()

#---坑位2：函数参数（超常见）
print("\n---【坑2】把列表传进函数---")
def add_item_bad(lst):
    """直接往传入的列表加东西- 有副作用"""
    lst.append("new")
    return lst


def add_item_good(lst):
    """先复制再加 -- 无副作用"""
    new_lst = lst.copy()
    new_lst.append("new")
    return new_lst


#测试bad版本
original = ["a","b"]
result = add_item_bad(original)
print("bad - original:",original)
print("bad - result:",result)

#测试good版本
original = ["a","b"]
result = add_item_good(original)
print("good - original:",original)
print("good - result:",result)

#----坑位3:循环中修改列表（最隐蔽）
print("\n---【坑3】循环中修改列表---")
#需求：从列表里删掉所有偶数
#错误做法：遍历时删除
nums = [1,2,3,4,5,6]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print("错误做法结果：",nums)

#正确做法1:遍历副本
nums = [1,2,3,4,5,6]
for n in nums.copy():
    if n %2 == 0:
        nums.remove(n)
print("正确做法1:",nums)

#正确做法2（推荐）：用列表推导生成新列表
nums = [1,2,3,4,5,6]
nums = [n for n in nums if n % 2 != 0]
print("正确做法2:",nums)
