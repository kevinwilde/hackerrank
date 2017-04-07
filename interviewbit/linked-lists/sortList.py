# Sort a linked list in O(n log n) time using constant space complexity.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def getSize(A):
    size = 0
    cur = A
    while cur:
        size += 1
        cur = cur.next
    return size

def splitInHalf(A, size):
    B = A
    prev = None
    i = 0
    while B and i < size/2:
        prev = B
        B = B.next
        i += 1
    if prev:
        prev.next = None
    return A, B

def merge(A, B):
    curA = A
    curB = B
    prev = None
    head = None
    while curA and curB:
        if curA.val < curB.val:
            cur = curA
            curA = curA.next
        else:
            cur = curB
            curB = curB.next
        if prev:
            prev.next = cur
        else:
            head = cur
        prev = cur
    while curA:
        if prev:
            prev.next = curA
        else:
            head = curA
        prev = curA
        curA = curA.next
    while curB:
        if prev:
            prev.next = curB
        else:
            head = curB
        prev = curB
        curB = curB.next
    return head

def sortList(A, size=None):
    if not size:
        size = getSize(A)
    if size == 1:
        return A
    A, B = splitInHalf(A, size)
    h1 = sortList(A, size/2)
    if size & 1:
        h2 = sortList(B, size/2+1)
    else:
        h2 = sortList(B, size/2)
    return merge(h1, h2)

### Tests

# 5 -> 9 -> 7 -> 3 -> 8 -> 10
a = ListNode(5)
b = ListNode(9)
c = ListNode(7)
d = ListNode(3)
e = ListNode(8)
f = ListNode(10)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
answer = [3, 5, 7, 8, 9, 10]
i = 0
cur = sortList(a)
for i in range(len(answer)):
    assert cur.val == answer[i]
    cur = cur.next
