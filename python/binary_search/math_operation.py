def sqrt_x(num):
    left, right = 0, num
    res = 0

    while left <= right:
        mid = left + ((right - 1) // 2)

        if mid ** 2 > num:
            right = mid - 1
        elif mid ** 2 < num:
            left = mid + 1
            res = mid
        else: 
            return mid
    return res


print(sqrt_x(4))
