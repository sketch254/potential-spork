def findPeakElement(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return i

    return len(nums) - 1


print(findPeakElement([1,3,6,8,3]))
