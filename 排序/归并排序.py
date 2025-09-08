def merge_sort(nums:list)->list:
    if len(nums)==1:
        return nums
    mid = len(nums)//2
    left_half  = merge_sort(nums[:mid])
    right_half = merge_sort(nums[mid:])
    return merge(left_half,right_half)

def merge(left:list,right:list)->list:
    result = []
    i,j = 0,0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
    '''
    while i<len(left):
        result.append(left[i])
        i+=1
    while j<len(right):
        result.append(right[j])
        j+=1
    return result
'''
nums = [9,8,8,7,6,6,5,4,1,2,3,4,0,0,2,3,5,2,1,0,0,2,4]
print(merge_sort(nums))


