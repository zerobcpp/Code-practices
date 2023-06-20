# 1161. Maximum Level Sum of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = []
        st = deque([root])
        val = 0
        while st:
            n = len(st)
            temp = [] 
            for i in range(n):
                node = st.popleft()
                temp.append(node.val)
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
            res.append(temp)
            
        val = -10 ** 5
        ret = 0
        n = len(res)
        
        for i in range(n):
            if val < sum(res[i]):
                val = sum(res[i])
                ret = i
        
        return ret + 1
        
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = []
        st = deque([root])
        val = -float('inf')
        ret = 0
        level = 0
        while st:
            n = len(st)
            tval = 0
            level += 1
            for i in range(n):
                node = st.popleft()
                tval += (node.val)
                if node.left:
                    st.append(node.left)
                if node.right:
                    st.append(node.right)
            if tval > val:
                val = tval
                ret = level
            
        
        return ret