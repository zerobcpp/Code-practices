# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        x = head
        while x:
            if x in seen:
                return True
            seen.add(x)
            x = x.next
        print(len(seen), seen)
        if len(seen) <= 1:
            return False
        return False