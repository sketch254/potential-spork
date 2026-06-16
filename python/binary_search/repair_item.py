import math

def repair_cars(ranks, cars):
    # base case scenario
    if len(ranks) <= 0:
        return

    def repaired(time):
        count = 0
        for r in ranks:
            count += int(math.sqrt(time // r))
        return count

    low, high = 1, ranks[0] * cars * cars
    res = -1

    while low < high:
        mid = (low + high) // 2
        repaired_cars = repaired(mid)

        if repaired_cars >= cars:
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res


print(repair_cars([], 10))
