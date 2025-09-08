def binary_search(nums:list, target:int)->int:
    left = 0
    right = len(nums)-1
    while left <=right :
        mid =  (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid]>target:
            right = mid-1
        elif nums[mid]<target:
            left = mid+1
    return -1
    
nums = [1,2,3,5,6,7,9,12,34,56,78,99]
target = 123
print(binary_search(nums,target))

