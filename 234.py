# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        copy = []
        x = head
        while x:
            copy.append(x.val)
            x = x.next
        
        return copy == copy[::-1]