# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        st = []
        def helper(node):
            if not node:
                return
            helper(node.left)
            st.append(node.val)
            helper(node.right)
        
        helper(root)
        def create(left, right):
            if left > right:
                return None
            mid = left + (right - left) // 2
            left = create(left, mid-1)
            right = create(mid+1, right)
            n = TreeNode(st[mid])
            
            n.left = left
            n.right = right
            return n
        
        st.sort()
        res = create(0, len(st)-1)
        
        #print(res)
        return res
        