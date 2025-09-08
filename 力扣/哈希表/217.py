def count(nums):
    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(count([1, 2, 2, 3, 3, 3]))
# 输出: {1: 1, 2: 2, 3: 3}
# 统计列表中每个元素出现的次数，并以字典形式返回结果