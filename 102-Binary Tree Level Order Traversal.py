# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # bfs
        if not root:
            return []
        res = []
        queue = deque([root])
        
        while queue:
            size = len(queue)
            inner = []
            for i in range(size):
                curr = queue.popleft()
                
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                
                inner.append(curr.val)
            res.append(inner)
        
        return res