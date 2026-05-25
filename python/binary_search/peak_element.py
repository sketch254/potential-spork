def findPeakElement(nums):


    curr_peak = 0
    iter = len(nums) - 1


    for i in range(iter):
        if nums[i] < nums[i + 1]:
            curr_peak = max(curr_peak, nums[i + 1])
        elif curr_peak < nums[i + 1]:
            curr_peak = max(curr_peak, nums[i + 1])
    return curr_peak



print(findPeakElement([1,6,8,3,5,6,7,90]))
