# 题 1：列表去重（保持原顺序）
# ============================================
# 需求：给一个列表，返回去重后的列表，且保持元素原来的顺序
# 限制：不许直接用 set() 转换（会丢顺序）
# 示例：[3, 1, 2, 3, 1, 4] → [3, 1, 2, 4]

def dedup(lst):
    # todo:在这里写你的实现
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result
    
    

#测试
print("题1 测试：")
print(dedup([3,1,2,3,1,4]))
print(dedup([]))
print(dedup([1,1,1,1]))
print(dedup(["a","b","a","c","b"]))


# ============================================
# 题 2：列表交集（保持第一个列表的顺序）
# ============================================
# 需求：给两个列表 a 和 b，返回"同时在 a 和 b 里"的元素
# 要求：保持 a 的顺序，且结果去重
# 示例：a=[3,1,4,1,5], b=[1,5,9,2,6] → [1, 5]

def intersect(a,b):
    result1 = []
    for item in a:
        if item in b and item not in result1:
            result1.append(item)
    return  result1
    

#测试
print("\n题 2 测试：")
print(intersect([3,1,4,1,5],[1,5,9,2,6]))
print(intersect([1,2,3],[4,5,6]))
print(intersect(["a","b","c"],["b","c","d"]))

# 题 3：嵌套列表扁平化（一层）
# ============================================
# 需求：把 [[1,2],[3,4],[5]] 变成 [1,2,3,4,5]
# 提示：思考 append 和 extend 的区别

def flatten(lst):
    result2 = []
    for sub in lst:
        result2.extend(sub)
    
    return result2

#测试
print("\n题 3 测试：")
print(flatten([[1,2],[3,4],[5]]))
print(flatten([[],[1],[2,3]]))
print(flatten([["a","b"],["c"]]))

# 题 4：筛选成年 active 用户（真实接口场景）
# ============================================
# 需求：接口返回用户列表，筛选出 age >= 18 且 status 为 'active' 的用户名
# 要求：用列表推导一行写完

users = [
    {"name": "Alice", "age": 25, "status": "active"},
    {"name": "Bob", "age": 17, "status": "active"},
    {"name": "Carol", "age": 30, "status": "inactive"},
    {"name": "Dave", "age": 22, "status": "active"},
    {"name": "Eve", "age": 16, "status": "inactive"},
]

def filter_users(users):
    # todo :用列表推导
    # result = []
    # for item in users:
    #     if item["age"] >= 18 and item["status"] == "active":
    #         result.append(item["name"])
    return [ item["name"] for item in users if item["age"] >= 18 and item["status"] == "active"]
    

#测试
print("\n题 4 测试")
print(filter_users(users))
