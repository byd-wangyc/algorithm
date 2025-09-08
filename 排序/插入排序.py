def insertion_sort(nums:list)->list:
    n = 1
    while n<len(nums):
        j = n
        while j>0:
            if nums[j]<nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]
            j-=1
        n+=1
    return nums

nums = [9,8,8,7,6,6,5,4,1,2,3,4,0,0,2,3,5,2,1,0,0,2,4]
print(insertion_sort(nums))
