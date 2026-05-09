# ============================================
# 字符串常用方法 · 按频率分类
# ============================================


# ============================================
# 高频组 1：清洗 - 测试代码里 70% 用得上
# ============================================


print("=== 高频组 1：清洗 ===")

# strip / lstrip / rstrip - 去除首尾空白字符

raw = "  hello world  \n"
print(repr(raw))                    # '  hello world  \n'
print(repr(raw.strip()))            # 'hello world' (去掉两端空白和换行)
print(repr(raw.lstrip()))           # 'hello world  \n' (只去左)
print(repr(raw.rstrip()))           # '  hello world' (只去右)

# strip 还可以指定要去掉的字符
url = "https://api.example.com/"
print(url.strip("/"))               # 'https://api.example.com' (去左右两端的 /)
print(url.rstrip("/"))              # 'https://api.example.com' (只去右边)


# replace - 替换内容（常用于清洗数据）

text = "phone: 138-1234-5678"
clean = text.replace("-", "")       # 把所有 - 替换成空
print(clean)                        # 'phone: 13812345678'

# replace 的第三个参数：限定只替换前 N 个
text = "aaa bbb aaa ccc aaa"
print(text.replace("aaa", "X", 2))  # 'X bbb X ccc aaa' (只替换前 2 个)


# ============================================
# 高频组 2：判断 - 测试断言常用
# ============================================


print("\n=== 高频组 2：判断 ===")

# 判断包含
text = "Error: user not found"
print("not found" in text)          # True
print("success" in text)            # False

# startswith / endswith - 判断开头结尾
url = "https://api.example.com/users"
print(url.startswith("https://"))   # True (是不是 HTTPS 协议)
print(url.endswith("/users"))       # True (是不是用户接口)

# 可以传 tuple 一次判断多个
filename = "report.pdf"
print(filename.endswith((".pdf", ".doc", ".docx")))   # True (是文档类型)

# isdigit / isalpha / isalnum - 判断字符类型
print("12345".isdigit())            # True (全是数字)
print("abc".isalpha())              # True (全是字母)
print("abc123".isalnum())           # True (字母+数字)
print("abc 123".isalnum())          # False (有空格)


# ============================================
# 高频组 3：分割与连接 - 处理数据必备
# ============================================


print("\n=== 高频组 3：分割与连接 ===")

# split - 把字符串切成 list

csv_line = "Alice,25,active"
fields = csv_line.split(",")        # 按 , 切
print(fields)                        # ['Alice', '25', 'active']

# 不传参数则按空白字符切（空格、tab、换行都算）
text = "hello   world  python"     # 多个空格
print(text.split())                  # ['hello', 'world', 'python']

# 限制切几次
log = "2024-01-01 ERROR Connection failed"
parts = log.split(" ", 2)            # 最多切成 3 部分
print(parts)                          # ['2024-01-01', 'ERROR', 'Connection failed']

# splitlines - 按换行切

text = "line1\nline2\nline3"
print(text.splitlines())             # ['line1', 'line2', 'line3']


# join - list 拼成字符串
words = ["Python", "is", "awesome"]
print(" ".join(words))               # 'Python is awesome'
print("-".join(words))               # 'Python-is-awesome'
print("".join(words))                # 'Pythonisawesome' (无分隔符)

# 注意：join 只能连接字符串列表，数字会报错
nums = [1, 2, 3]
# print(",".join(nums))              # ❌ TypeError
print(",".join(str(n) for n in nums))   # ✓ '1,2,3' (先转字符串)


# ============================================
# 高频组 4：大小写与格式
# ============================================


print("\n=== 高频组 4：大小写 ===")

s = "Hello World"
print(s.upper())                    # 'HELLO WORLD'
print(s.lower())                    # 'hello world'
print(s.title())                    # 'Hello World' (每个单词首字母大写)
print(s.capitalize())               # 'Hello world' (只有第一个字母大写)
print(s.swapcase())                 # 'hELLO wORLD' (大小写互换)


# ============================================
# 中频组：查找位置
# ============================================


print("\n=== 中频组：查找 ===")

s = "Hello, World"

# find - 找子串位置，找不到返回 -1
print(s.find("World"))              # 7
print(s.find("Python"))             # -1 (找不到)

# index - 同 find，但找不到会报错（适合"必须存在"的场景）
print(s.index("World"))             # 7
# print(s.index("Python"))          # ❌ ValueError

# count - 出现几次
print("hello world".count("l"))     # 3


# ============================================
# 实战场景演示
# ============================================


print("\n=== 实战场景 ===")


# 场景 1：从 URL 提取路径段
url = "https://api.example.com/v1/users/123/orders"
parts = url.split("/")
print(parts)                         # ['https:', '', 'api.example.com', 'v1', 'users', '123', 'orders']
# 取出用户 ID
user_id = parts[5]
print(f"用户 ID: {user_id}")


# 场景 2：清洗接口返回的脏数据
raw_name = "  Alice \n"
clean_name = raw_name.strip()
print(f"清洗后: {repr(clean_name)}")    # 'Alice'


# 场景 3：判断文件类型
filename = "report_2024.xlsx"
if filename.endswith(".xlsx"):
    print("这是 Excel 文件")
elif filename.endswith(".pdf"):
    print("这是 PDF 文件")


# 场景 4：解析 query string
query = "name=Alice&age=25&city=NYC"
pairs = query.split("&")             # ['name=Alice', 'age=25', 'city=NYC']
result = {}
for pair in pairs:
    key, value = pair.split("=")     # 解包！tuple 那节学过
    result[key] = value
print(result)                         # {'name': 'Alice', 'age': '25', 'city': 'NYC'}


# 场景 5：构造 SQL where 条件
columns = ["name", "age", "city"]
values = ["Alice", "25", "NYC"]

# 生成 "name='Alice' AND age='25' AND city='NYC'"
conditions = [f"{c}='{v}'" for c, v in zip(columns, values)]
print(conditions)
where_clause = " AND ".join(conditions)
print(where_clause)