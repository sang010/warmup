s = "Hello, World"
#身份1，一段文字
print("身份1:一段文字")
print(s)
print(f"长度：{len(s)}")
print(f"是否包含World:{'World' in s}")

#身份2:一串字符的序列（结构层面）
print("\n身份：字符序列")

print(s[0])
print(s[-1])
print(s[7])

#可以切片
print(s[0:5])
print(s[7:])
print(s[::-1])

#可以遍历每个字符
for char in s[:5]:
    print(f"字符：{char}")
#关键差异：string是不可变的
print("\n关键差异：string不可变")

original = "hello"
modified = original.replace("h","H")

print(f"original = {original}")
print(f"modified = {modified}")

print(f"original 的id：{id(original)}")
print(f"modified 的id：{id(modified)}")

#字符串不可变的实际含义
print("\n字符串不可变一位置：")
s = "hello"
print(f"s.upper() = {s.upper()}")
print(f"s 还是 = {s}")
s = s.upper()
print(f"重新赋值后 s = {s}")

print("\n字符串拼接")
greeting = "Hello, " + "World"
print(greeting)

#join
words = ["Hello","World","Python"]
joined = " ".join(words)
print(joined)

joined = ", ".join(words)
print(joined)