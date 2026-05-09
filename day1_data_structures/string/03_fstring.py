# ============================================
# f-string · Python 字符串格式化的最佳方式
# ============================================


# --- 1. 基础用法 ---


print("=== 基础用法 ===")

name = "Alice"
age = 25

# f-string：在字符串前加 f，{}里写变量名
print(f"姓名: {name}, 年龄: {age}")
# 姓名: Alice, 年龄: 25


# 对比传统写法（已经过时，了解即可）：

# 方式 1：% 格式化（很老）
print("姓名: %s, 年龄: %d" % (name, age))

# 方式 2：.format()（也过时了）
print("姓名: {}, 年龄: {}".format(name, age))

# 方式 3：f-string（现代标准，推荐）
print(f"姓名: {name}, 年龄: {age}")

# 三种结果一样，但 f-string 最简洁、最快、最易读


# --- 2. {} 里可以放任何 Python 表达式 ---


print("\n=== {} 里可以放表达式 ===")

x = 5
y = 3

# 算术运算
print(f"{x} + {y} = {x + y}")
print(f"{x} 的平方是 {x ** 2}")

# 调用方法
name = "alice"
print(f"大写: {name.upper()}")

# 三元表达式
score = 85
print(f"成绩: {score} 分，{'及格' if score >= 60 else '不及格'}")

# 访问字典
user = {"name": "Bob", "age": 30}
print(f"用户名: {user['name']}, 年龄: {user['age']}")
# 注意：里面用单引号 '，外面用双引号 "，不要冲突

# 索引和切片
fruits = ["apple", "banana", "cherry"]
print(f"第一个水果: {fruits[0]}, 最后一个: {fruits[-1]}")


# --- 3. 数字格式化（极常用！）---


print("\n=== 数字格式化 ===")

# 保留小数位
pi = 3.14159265
print(f"pi ≈ {pi:.2f}")            # 3.14   保留 2 位小数
print(f"pi ≈ {pi:.4f}")            # 3.1416 保留 4 位小数
print(f"pi ≈ {pi:.0f}")            # 3      不保留小数

# 千位分隔符（财务报表常用）
big_num = 1234567
print(f"金额: {big_num:,}")        # 1,234,567

# 百分比
ratio = 0.8567
print(f"准确率: {ratio:.2%}")       # 85.67%
print(f"准确率: {ratio:.0%}")       # 86%

# 科学计数法
small = 0.0000123
print(f"小数: {small:.2e}")        # 1.23e-05


# --- 4. 字符串对齐和填充 ---


print("\n=== 对齐和填充 ===")

name = "Alice"

# 默认右对齐
print(f"|{name:>10}|")              # |     Alice|（10 字符宽，右对齐）

# 左对齐
print(f"|{name:<10}|")              # |Alice     |

# 居中
print(f"|{name:^10}|")              # |  Alice   |

# 用其他字符填充
print(f"|{name:*>10}|")             # |*****Alice|（用 * 填充）
print(f"|{name:->10}|")             # |-----Alice|（用 - 填充）


# 数字补 0（生成订单号、ID 常用）
order_id = 42
print(f"ORDER-{order_id:0>6}")      # ORDER-000042 （前面补 0 到 6 位）
print(f"ORDER-{order_id:06d}")      # ORDER-000042 （等价写法，更简洁）


# --- 5. 调试神器：变量名=值 ---


print("\n=== 调试神器：变量名=值 ===")

# Python 3.8+ 引入的功能，调试时巨好用

x = 10
y = 20

# 普通方式
print(f"x={x}, y={y}")              # x=10, y=20

# 用 = 自动显示变量名（Python 3.8+）
print(f"{x=}, {y=}")                # x=10, y=20  （省力！）

# 调试复杂表达式
nums = [1, 2, 3, 4, 5]
print(f"{len(nums)=}")              # len(nums)=5
print(f"{sum(nums)=}")              # sum(nums)=15
print(f"{max(nums)=}")              # max(nums)=5

# 这个特性在调试时极其有用：
# 不用再写 print("nums =", nums)，直接 print(f"{nums=}")


# --- 6. 多行 f-string ---


print("\n=== 多行 f-string ===")

# 三引号 + f 可以写多行
name = "Alice"
age = 25
city = "NYC"

info = f"""
姓名: {name}
年龄: {age}
城市: {city}
"""
print(info)


# --- 7. 实战场景 ---


print("\n=== 实战场景 ===")


# 场景 1：构造日志消息
user = "alice"
action = "login"
status = "success"
import datetime
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
log = f"[{now}] user={user} action={action} status={status}"
print(log)


# 场景 2：构造 SQL/API 参数（注意：实际项目要用参数化查询防 SQL 注入）
table = "users"
where_id = 123
print(f"SELECT * FROM {table} WHERE id={where_id}")


# 场景 3：测试报告
test_name = "test_login"
duration = 1.234
status = "PASSED"
print(f"{test_name:<30} {duration:>6.2f}s  [{status}]")


# 场景 4：进度显示
done = 23
total = 100
print(f"进度: {done}/{total}  ({done/total:.1%})")


# 场景 5：测试数据生成
for i in range(1, 6):
    test_user = f"test_user_{i:03d}"     # test_user_001, test_user_002, ...
    print(test_user)