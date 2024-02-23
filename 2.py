# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):    
        l1 = [2, 4, 3]
        l2 = [5, 6, 4]
        
        l1.reverse()
        l2.reverse()
        a = ""
        b = ""
        
        for i in l1:
            a = a + str(i)
        
        for j in l2:
            b = b + str(j)
        
        print(int(a) + int(b))
