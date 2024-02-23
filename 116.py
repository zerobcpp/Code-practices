"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root):
        """
        :type root: TreeLinkNode
        :rtype: nothing
        """
        if not root:
            return None
        
        curr = root
        reset = root.left
        
        while curr.left:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left 
                curr = curr.next
            else:
                curr = reset
                reset = curr.left
        return root