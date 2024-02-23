# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def dfs(node, path):
            if not node:
                return
            path[node.val] += 1
            if not node.left and not node.right:
                cond = [False, False, False] # 1 cnt, 1cnt, 2cnt                
                for i, v in path.items():
                    if v % 2 == 1 and cond[0] == False:
                        cond[0] = True
                    elif v % 2 == 1 and cond[0] == True:
                        cond[1] = True
                    if v % 2 == 0:
                        cond[2] = True
                
                #print(path, cond)
                if (cond[0] == True and cond[1] == False and cond[2] == True) or (cond[0] and not cond[1] and not cond[2]) or (cond[2] and not cond[0] and not cond[1]):
                    self.res += 1
                
                #print()
            for child in [node.left, node.right]:
                if child:
                    dfs(child, path)
            path[node.val] -= 1
        
        
        dfs(root, defaultdict(int) )
        
        return self.res
                    
    def pseudoPalindromicPaths1(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        
        def dfs(node, path):
            if not node:
                return
            path ^= (1 << node.val)
            if not node.left and not node.right:
                if path & (path - 1) == 0:
                    self.res += 1
            
            for child in [node.left, node.right]:
                if child:
                    dfs(child, path)
        
        dfs(root, 0)
        return self.res
        

        
# a a b a a 
# a b c b a
# r a c e c a r 

# 9 1 5 5 5 5 1 9 