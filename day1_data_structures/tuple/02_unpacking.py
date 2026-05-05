#1基础解包
point = (3,5)
x,y = point
print(f"x = {x},y = {y}")

#tuple  也可以解包到list
nums = [10,20,30]
a,b,c = nums
print(f"a={a},b={b},c={c}")

#3函数返回多个值 = 返回一个tuple

def get_user_info():
    """获取用户信息"""
    name = "Alice"
    age = 25
    email = "alice@example.com"
    return name,age,email

#解包接收
name,age,email = get_user_info()
print(f"\n姓名：{name},年龄：{age},邮箱：{email}")

#也可以接收为一个 tuple
info = get_user_info()
print(f"info类型：{type(info)}")
print(f"info:{info}")
print(f"姓名:{info[0]}")


#4交换两个变量
a = 1
b = 2
print(f"\n交换前：a={a},b={b}")
a,b= b,a
print(f"交换后:a={a},b={b}")

#5配合enumerate
fruits = ["appel","banana","cherry"]

#传统写法
for i in range(len(fruits)):
    print(f"{i}:{fruits[i]}")
print()

for index,fruit in enumerate(fruits):
    print(f"{index}:{fruit}")

#配合字典遍历
user = {"name":"Alice","age":25,"email":"alice@example.com"}

#d.items()返回每个（key，value）对，是tuple
for key,value in user.items():
    print(f"{key} = {value}")

#7配合zip
names = ["Alice","Bob","Carol"]
ages = [25,30,22]

#zip把多个序列“拉链式”组合
for name,age in zip(names,ages):
    print(f"{name}今年{age}岁")

#8.星号解包：抓住剩下的
#把第一个和最后一个分开，中间的打包成list
first,*middle,last= nums
print(f"\nfirst = {first}")
print(f"middle = {middle}")
print(f"last = {last}")

#星号变量永远是list，不是tuple
#只要第一个，剩下的不要
first,*rest = [10,20,30,40]
print(f"first = {first},rest = {rest}")

#只要最后一个
*head,last = [10,20,30,40]
print(f"head = {head},last = {last}")

#真实测试场景
def parse_response(response):
    """模拟解析接口响应，返回（是否成功，数据，错误信息"""
    if response.get("code") == 0:
        return True,response.get("data"),None
    else:
        return False,None,response.get("msg","unknown error")

#解包接收
success,data,error = parse_response({"code":0,"data":[1,2,3]})
print(f"\n成功：{success},数据：{data},错误：{error}")
success,data,error = parse_response({"code":1,"msg":"user not found"})
print(f"成功：{success},数据：{data},错误：{error}")