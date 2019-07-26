# -*- coding: utf-8 -*-


def find_min(nums: list) -> int:
    l, r = 0, len(nums) - 1
    if nums[l] < nums[r]: # nothing is rotated
        return nums[l]
    while l <= r:
        mid = (l + r) // 2
        if nums[l] == nums[r] and nums[mid] == nums[l]:
            return find_min_in_order(nums)
        if nums[l] < nums[mid]:
            l = mid
        elif nums[r] > nums[mid]:
            r = mid
        else:
            return nums[r]

def find_min_in_order(nums: list) -> int:
    minVal = nums[0]
    for i in range(1, len(nums)):
        if nums[i] < minVal:
            minVal = nums[i]
    return minVal

lst = [3,4,5,1,2]
lst1 = [3,4,5,0,1,2]
lst2 = [1,0,1,1,1]
print(find_min(lst))
print(find_min(lst1))
print(find_min(lst2))
