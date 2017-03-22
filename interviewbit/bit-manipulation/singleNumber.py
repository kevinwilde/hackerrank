# Given an array of integers, every element appears twice except for one.
# Find that single one

# @param A : tuple of integers
# @return an integer
def singleNumber(A):
    ans = 0
    for num in A:
        ans ^= num
    return ans

assert singleNumber([1,2,2,3,1]) == 3
assert singleNumber([1,2,2,4,1]) == 4
assert singleNumber([1,2,3,3,1]) == 2
assert singleNumber([1,0,2,1,2]) == 0
