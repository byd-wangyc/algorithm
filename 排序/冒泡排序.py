def bubble_sort(nums:list)->list:
    length= len(nums)
    while length>1:
        for j in range(1,length):
            if nums[j]<nums[j-1]:
                nums[j],nums[j-1] = nums[j-1],nums[j]
        length = length -1
    return nums

nums = [9,8,8,7,6,6,5,4,1,2,3,4,0,0,2,3,5,2,1,0,0,2,4]
print(bubble_sort(nums))
