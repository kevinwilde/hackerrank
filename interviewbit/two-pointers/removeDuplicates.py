# @param A : list of integers
# @return an integer
def removeDuplicates(A):
    size = 0
    i = 0
    while i < len(A):
        A[size] = A[i]
        size += 1
        i += 1
        while i < len(A) and A[i]==A[i-1]:
            i += 1
    return size

A = [0,0,1,2,2,3,3,3,3]
size = removeDuplicates(A)
assert size == 4
assert A[:size] == [0,1,2,3]
