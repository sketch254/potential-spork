def minimizeMax(nums, p):
    nums.sort()

    def can_form(max_diff):
        count, i = 0, 0
        while i < len(nums) - 1:
            if nums[i + 1] - nums[i] <= max_diff:
                count += 1
                i += 2
            else:
                i += 1

        return count >= p

    low, high = 0, nums[-1] - nums[0]

    while low < high:
        mid = low + ((high - low) // 2)
        if can_form(mid):
            high = mid
        else:
            low += 1

    return low


print(minimizeMax([10,1,2,7,1,3, 6], 2))