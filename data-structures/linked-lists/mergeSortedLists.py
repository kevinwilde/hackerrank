"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def MergeLists(headA, headB):
    if headA == None:
        return headB
    if headB == None:
        return headA
    if headA.data < headB.data:
        mergeHelper(headA.next, headB, headA)
        return headA
    else:
        mergeHelper(headA, headB.next, headB)
        return headB
    
def mergeHelper(n1, n2, cur):
    if n1 == None:
        cur.next = n2
        return
    if n2 == None:
        cur.next = n1
        return
    if n1.data < n2.data:
        cur.next = n1
        mergeHelper(n1.next, n2, n1)
    else:
        cur.next = n2
        mergeHelper(n1, n2.next, n2)  
