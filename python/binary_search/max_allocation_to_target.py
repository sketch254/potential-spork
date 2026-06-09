def maxResourceAllocation(candies, target):

    if sum(candies) < target:
        return 0

    def can_allocate(num):
        x = sum(piles// num for piles in candies) 
        return x >= target

    low, high = 0, max(candies)
    res = 0

    while low < high:
        mid = (low + high) // 2
        if can_allocate(mid):
            res = mid
            low = mid + 1

        else:
            high = mid - 1

    return res

    

print(maxResourceAllocation([6, 6, 6], 3))
