def twoSum(nums: list[int], target: int):
    list1 = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                list1.append(i)
                list1.append(j)
                return list1


nums = [2, 7, 11, 15, 19]
target = 9
print(twoSum(nums, target))
