# Given an array of integers, find two numbers such that they add up
# to a specific target number.

# @param A : tuple of integers
# @param k : integer
# @return a list of integers
def twoSum(A, k):
    seen = {}
    for idx, num in enumerate(A):
        if k - num in seen:
            return [seen[k-num], idx+1]
        if num not in seen:
            seen[num] = idx + 1
    return []

assert twoSum([2,7,11,15], 9) == [1,2]
assert twoSum([7,11,15,2], 9) == [1,4]

