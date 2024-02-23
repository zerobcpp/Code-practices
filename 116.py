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
        
        if not root or not root.left:
            return root
        
        left = root.left
        right = root.right
        left.next = right
        
        if root.next:
            right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        
        return root