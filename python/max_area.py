def maxArea(heights):
    res = 0
    for i in range(len(heights)):
        for j in range(i + 1, len(heights)):
            res = max(res, min(heights[i], heights[j]) * (j - i))
    return res


print(maxArea([1,2,3,4,5,6,7]))
