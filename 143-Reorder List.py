# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        st = []
        dummy = head
        cur = head
        while cur:
            st.append(cur)
            cur = cur.next
        N = len(st)
        for i in range(N//2):
            nxt = head.next
            head.next = st.pop()
            head = head.next
            head.next = nxt
            head = head.next
        
        if head:
            head.next = None
        #self.debug(dummy)
        
            
    
    def debug(self, head):
        node = head
        while node:
            print(node.val, end = '-->')
            node = node.next