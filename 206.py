# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        x = head
        prev = None
        
        
        if not head:
            return None
        else:
            while x is not None:
                y = x.next
                x.next = prev
                prev = x
                x = y
            return prev