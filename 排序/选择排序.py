def selection_sort(nums:list)->list:
    length = len(nums)
    for i in range(length):
        for j in range(i+1,length):
            if nums[j]<nums[i]:
                nums[i],nums[j] = nums[j],nums[i]
    return nums

nums = [9,8,8,7,6,6,5,4,1,2,3,4,0,0,2,3,5,2,1,0,0,2,4]
print(selection_sort(nums))

