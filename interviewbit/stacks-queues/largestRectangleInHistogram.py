def largestRectangleArea(A):
    s = []
    biggest = 0
    i = 0
    n = len(A)
    while i < n:
        if not s or A[i] > A[s[-1]]:
            s.append(i)
            i += 1
        else:
            height = A[s.pop()]
            width = i-s[-1]-1 if s else i
            area = height*width
            biggest = max(biggest, area)
    while s:
        height = A[s.pop()]
        width = n-s[-1]-1 if s else n
        area = height*width
        biggest = max(biggest, area)
    return biggest

A = [2,1,5,6,2,3]
print largestRectangleArea(A)

