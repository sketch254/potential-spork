import math

def arrangeCoins(n: int) -> int:
    k = int((-1 + math.sqrt(1 + 8 * n)) / 2)
    print(k)
    # sqrt can round wrong — check one step up
    if (k + 1) * (k + 2) // 2 <= n:
        k += 1
    return k


print(arrangeCoins(10))
