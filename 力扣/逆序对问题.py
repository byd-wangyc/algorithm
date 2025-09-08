# 返回逆序对的个数，要求时间复杂度O(nlogn)

def count_inversions(arr):
    """
    使用归并排序计算数组中的逆序对个数
    
    参数:
    arr: 输入数组
    
    返回:
    sorted_arr: 排序后的数组
    count: 逆序对的数量
    """
    # 递归终止条件：当数组长度为1或0时，直接返回
    if len(arr) <= 1:
        return arr, 0
    
    # 找到中间位置，将数组分成两部分
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # 递归地对左右两部分进行排序并计算逆序对
    left_sorted, left_count = count_inversions(left_half)
    right_sorted, right_count = count_inversions(right_half)
    
    # 合并两个已排序的部分并计算跨分割点的逆序对
    merged, cross_count = merge_and_count(left_sorted, right_sorted)
    
    # 总逆序对数量 = 左半部分逆序对 + 右半部分逆序对 + 跨分割点逆序对
    total_count = left_count + right_count + cross_count
    
    return merged, total_count

def merge_and_count(left, right):
    """
    合并两个已排序的列表并计算逆序对
    
    参数:
    left: 第一个已排序的列表
    right: 第二个已排序的列表
    
    返回:
    result: 合并后的有序列表
    count: 逆序对的数量
    """
    result = []
    i = j = 0
    count = 0
    
    # 比较两个列表的元素，将较小的元素添加到结果中
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
            count += len(right) - j

        else:
            result.append(right[j])
            j += 1
    
    # 将剩余的元素添加到结果中
    while i < len(left):
        result.append(left[i])
        i += 1
        
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result, count

# 测试示例
if __name__ == "__main__":
    # 测试用例
    test_arrays = [
        [1, 2, 3, 4, 5],          # 已排序数组，逆序对为0
        [5, 4, 3, 2, 1],          # 逆序数组，逆序对为10
        [2, 4, 1, 3, 5],          # 混合数组
        [1, 20, 6, 4, 5],         # 另一个混合数组
        [1],                      # 单元素数组
        [],                        # 空数组
        [3,1,2,0]
    ]
    
    for arr in test_arrays:
        sorted_arr, inversions = count_inversions(arr)
        print(f"数组: {arr}")
        print(f"排序后: {sorted_arr}")
        print(f"逆序对数量: {inversions}")
        print("-" * 30)

    

