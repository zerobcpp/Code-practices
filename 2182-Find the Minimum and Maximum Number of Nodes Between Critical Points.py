# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        cur = head
        res = []
        prev = None
        st = []
        location = 0
        mn = float('inf')
        while cur:
            if prev and cur.next:
                if cur.val > prev.val and cur.val > cur.next.val:
                    st.append(location)
                elif cur.val < prev.val and cur.val < cur.next.val:
                    st.append(location)
                if len(st) >= 2:
                    mn = min(mn, st[-1] - st[-2])
            
            location += 1
            prev = cur
            cur = cur.next
        
        #print(st)
        return [-1, -1] if len(st) < 2 else [mn, st[-1] - st[0]]