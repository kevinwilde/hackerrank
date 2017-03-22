# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def insertionSortList(self, A):
        cur = A
        newList = None
        while cur:
            toBeNext = cur.next
            cmpr = newList
            prev = None
            while cmpr and cur.val > cmpr.val:
                prev = cmpr
                cmpr = cmpr.next
            cur.next = cmpr
            if prev:
                prev.next = cur
            else:
                newList = cur
            cur = toBeNext
        return newList

