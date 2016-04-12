"""
Check if linked list has cycle
head could be None as well for empty list
Node is defined as

class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

returns 0 if no cycle else return 1
"""
def HasCycle(head):
    fast = head
    slow = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return 1
    return 0
