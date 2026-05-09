# ============================================
# string 练习题 · 独立完成
# ============================================


# ============================================
# 题 1：解析 query string
# ============================================
# 需求：把 URL 的 query 部分解析成字典
# 示例：
#   "name=Alice&age=25&city=NYC"
#   → {"name": "Alice", "age": "25", "city": "NYC"}
#
# 提示：
# - 先用 split("&") 切成几段
# - 每段再用 split("=") 切成 key 和 value
# - 用 tuple 解包 + 字典存储


def parse_query(qs):
    # TODO
    paris = qs.split("&")
    result = {}
    for pari in paris:
        key,value = pari.split("=")
        result[key] = value
    return result
    


# 测试
print("题 1 测试:")
print(parse_query("name=Alice&age=25&city=NYC"))
# 预期：{'name': 'Alice', 'age': '25', 'city': 'NYC'}

print(parse_query("user=bob&active=true"))
# 预期：{'user': 'bob', 'active': 'true'}


# ============================================
# 题 2：判断回文
# ============================================
# 需求：判断字符串是否是回文（正着读和反着读一样）
# 要求：忽略大小写、忽略空格
# 示例：
#   "A man a plan a canal Panama" → True
#   "hello" → False
#   "Race car" → True
#
# 提示：
# - 先把字符串处理成"干净版"：去空格 + 转小写
# - 然后判断和它的反转是否相等
# - 反转字符串：s[::-1]


def is_palindrome(s):
    
    cleaned = s.replace(" ","").lower()
    return cleaned == cleaned[::-1]

    

    


# 测试
print("\n题 2 测试:")
print(is_palindrome("A man a plan a canal Panama"))   # True
print(is_palindrome("hello"))                          # False
print(is_palindrome("Race car"))                       # True
print(is_palindrome(""))                                # True (空字符串是回文)


# ============================================
# 题 3：测试报告格式化（综合应用）
# ============================================
# 需求：根据测试结果列表，输出格式化的测试报告
# 数据格式：每条记录是 (用例名, 耗时, 是否通过)
#
# 期望输出（注意对齐）：
#   ============================================================
#   测试报告
#   ============================================================
#   test_login                              1.23s   [PASSED]
#   test_register                          12.45s   [FAILED]
#   test_logout                             0.05s   [PASSED]
#   ============================================================
#   总计: 3 个用例，通过 2 个，失败 1 个，通过率 66.67%
#   ============================================================


tests = [
    ("test_login", 1.23, True),
    ("test_register", 12.45, False),
    ("test_logout", 0.05, True),
]


def print_report(tests):
    """
    提示：
    - 用例名左对齐占 30 字符宽：{name:<30}
    - 耗时右对齐占 6 字符宽，保留 2 位小数：{duration:>6.2f}
    - 用 "=" * 60 生成分隔线（60 个等号）
    - 通过率用百分比格式：{rate:.2%}
    - True/False 转 "PASSED"/"FAILED" 可以用三元表达式
    """
    print("="*60)
    print("测试报告")
    print("="*60)

    passed = 0
    failed = 0
    for name,duration,is_pass in tests:
        status = "PASSED" if is_pass else "FAILED"
        print(f"{name:<30}{duration:>6.2f}s [{status}]")

        if is_pass:
            passed += 1
        else:
            failed += 1
    
    print("="*60)

    total = len(tests)
    rate = passed/total
    print(f"总计：{total}个用例，通过{passed}个，失败{failed}个，通过率{rate:.2%}")
    
    print("="*60)




# 测试
print("\n题 3 测试:")
print_report(tests)