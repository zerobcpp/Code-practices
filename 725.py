# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        N = 0
        cur = head
        while cur:
            N += 1
            cur = cur.next
        
        length = N // k
        remain = N % k
        print(length, N, remain)
        res = []
        
        cur = head
        for i in range(k):
            temp = dummy = ListNode(-1)
            for j in range(length + (i < remain)):
                if not cur:
                    break
                n = ListNode(cur.val)
                temp.next = n
                temp = temp.next
                cur = cur.next
            res.append(dummy.next)
        
        return res