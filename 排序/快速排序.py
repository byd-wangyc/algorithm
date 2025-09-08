# 快速排序算法实现

import random
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[random.randint(0, len(arr) - 1)]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# 示例用法
nums = [9,8,8,7,6,6,5,4,1,2,3,4,0,0,2,3,5,2,1,0,0,2,4]
print(quick_sort(nums))
