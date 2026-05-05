# ============================================
# tuple 练习题 · 独立完成
# ============================================


# ============================================
# 题 1：函数返回多个值 + 解包
# ============================================
# 需求：写一个函数 get_min_max_avg(nums)
#       接收一个数字列表，返回 (最小值, 最大值, 平均值)
# 调用方应该能这样使用：
#       low, high, avg = get_min_max_avg([3, 1, 4, 1, 5, 9, 2, 6])
#       print(low, high, avg)   # 1 9 3.875
#
# 提示：
# - min(), max(), sum() 是 Python 内置函数
# - 平均值 = 总和 / 个数
# - return 多个值时直接用逗号隔开就行


def get_min_max_avg(nums):
    # TODO
    avg = sum(nums) / len(nums)
    return min(nums),max(nums),avg
    


# 测试
print("题 1 测试:")
low, high, avg = get_min_max_avg([3, 1, 4, 1, 5, 9, 2, 6])
print(f"最小: {low}, 最大: {high}, 平均: {avg}")
# 预期：最小: 1, 最大: 9, 平均: 3.875

low, high, avg = get_min_max_avg([10, 20, 30])
print(f"最小: {low}, 最大: {high}, 平均: {avg}")
# 预期：最小: 10, 最大: 30, 平均: 20.0


# ============================================
# 题 2：用 tuple 当字典 key（真实场景）
# ============================================
# 需求：统计一组操作日志，每条日志记录了 (用户名, 操作类型)
#       要算出"每个用户做了每种操作多少次"
#
# 输入数据：
logs = [
    ("alice", "login"),
    ("bob", "login"),
    ("alice", "view"),
    ("alice", "view"),
    ("alice", "view"),
    ("bob", "logout"),
    ("alice", "login"),
    ("bob", "view"),
    ("alice", "logout"),
]

# 期望输出：一个字典，key 是 (用户名, 操作类型)，value 是次数
# {
#   ("alice", "login"): 2,
#   ("alice", "view"): 3,
#   ("alice", "logout"): 1,
#   ("bob", "login"): 1,
#   ("bob", "logout"): 1,
#   ("bob", "view"): 1,
# }


def count_operations(logs):
    """
    提示：
    - 创建一个空字典 result = {}
    - 遍历 logs，每条日志是一个 (user, action) tuple
    - 用 (user, action) 当作字典的 key
    - 如果 key 已存在 → 次数 +1
    - 如果 key 不存在 → 设为 1
    - 可以用 dict.get(key, 0) 拿到当前次数（不存在返回 0）
    """
    result1 = {}
    for key,value in logs:
        point = (key,value)
        print(point)
        if point in result1:
            result1[point] = result1[point] +1
        else:
            result1[point] = 1
    return result1
        

    


# 测试
print("\n题 2 测试:")
result = count_operations(logs)
for key, count in result.items():     # 解包遍历字典
    print(f"  {key}: {count}")