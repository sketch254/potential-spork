class ListReader:
    def __init__(self, arr):
        self.arr = arr

    def length(self):
        return len(self.arr)

    def compareSub(self, l, r, x, y):
        sum1 = sum(self.arr[l:r+1])
        sum2 = sum(self.arr[x:y+1])
        if sum1 < sum2: return -1
        if sum1 > sum2: return 1
        return 0


def getIndex(reader):
    left = 0
    length = reader.length()
    while length > 1:
        length //= 2
        cmp = reader.compareSub(left, left + length - 1, left + length, left + length + length - 1)
        if cmp == 0:
            return left + length + length
        if cmp < 0:
            left += length
    return left


reader = ListReader([1, 1, 1, 1, 1, 1, 1, 2])
print(getIndex(reader))  # Expected: 7
