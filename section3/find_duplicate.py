lst = [2,4,6,8,4,6]


def find_duplicate(nums: list) -> int:
    def count_range(i, j):
        return sum(i <= num <= j for num in nums)
            
    lo = 1
    hi = len(nums) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        print(lo, mid, hi)
        count = count_range(lo, mid)
        if lo == hi:
            if count > 1:
                return lo
            else:
                break
        if count > mid - lo + 1:
            hi = mid
        else:
            lo = mid + 1
    return -1


# find_duplicate(lst)


def duplicates(nums: list) -> list:
    numDict = dict()
    returnLst = []
    for n in nums:
        numDict[n] = numDict.get(n, 0) + 1
        if numDict[n] > 1:
            returnLst.append(n)
    return returnLst


lst1 = [0,1,2,3,5,3]
lst2 = [2,3,1,0,2,5,3]

print(duplicates(lst1))
print(duplicates(lst2))

