from collections import defaultdict

def subArrayLength(nums, target):
    res = 0
    count = defaultdict(int)
    left = 0

    for right in range(len(nums)):
        count[nums[right]] += 1
        while count[nums[right]] > target:
            count[nums[left]] -= 1
            left += 1

        res = max(res, right - 1 + 1)

    return res


print(subArrayLength([1,2,3,1,2,3,1,2], 2))
