#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def swapPairs(head):
    if not head:
        return None
    cur = head
    dummy = ListNode(-1)
    dummy.next = head
    cur = dummy
    i = 0
    while cur.next and cur.next.next:
        one = cur.next
        two = cur.next.next
        cur.next = two
        
        one.next = two.next
        two.next = one
        
        #debug(dummy.next)
        
        
        cur = cur.next.next
    return dummy.next
    
def debug(node):
    cur = node
    while cur:
        print(cur.val, end = ', ')
        cur = cur.next

head = [1,2,3,4]
N = len(head)
dummy = ListNode(-1)
cur = dummy
for i in range(N):
    cur.next = ListNode(head[i])
    cur = cur.next

#debug(dummy)

swapPairs(dummy.next)