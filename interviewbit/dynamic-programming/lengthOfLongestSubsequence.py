"""
Given an array of integers, find the length of longest subsequence which
is first increasing then decreasing.
"""

def reverse(A):
    return A[::-1]

def longestDecreasingSubsequence(A):
        return reverse(longestIncreasingSubsequence(reverse(A)))

def longestIncreasingSubsequence(A):
    ans = [1 for _ in range(len(A))]
    for i in range (1 , len(A)):
        for j in range(0 , i):
            if A[i] > A[j] and ans[i] < ans[j] + 1:
                ans[i] = ans[j]+1
    return ans

def solve(A):
    inc = longestIncreasingSubsequence(A)
    dec = longestDecreasingSubsequence(A)
    best = 0
    for i in range(len(A)):
        best = max(best, inc[i]+dec[i]-1)
    return best

### Tests ###
A = [1, 11, 2, 10, 4, 5, 2, 1]
assert solve(A) == 6
A = [7, 6, 8, 10, 2, 5, 12, 30, 31, 20, 22, 18]
assert solve(A) == 8
