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
            if not node.left and not node.right:
                #print(path)
                c = defaultdict(int)
                for i in path: 
                    c[i] += 1
                cond = [False, False, False] # 1 cnt, 1cnt, 2cnt
                
                for i, v in c.items():
                    if v % 2 == 1 and cond[0] == False:
                        cond[0] = True
                    elif v % 2 == 1 and cond[0] == True:
                        cond[1] = True
                    if v % 2 == 0:
                        cond[2] = True
                
                if (cond[0] == True and cond[1] == False and cond[2] == True) or (cond[0] and not cond[1] and not cond[2]):
                    self.res += 1
                
                #print()
                
            for child in [node.left, node.right]:
                if child:
                    dfs(child, path + [child.val])
        
        dfs(root, [root.val])
        
        return self.res
                    
        
        
        

        
# a a b a a 
# a b c b a
# r a c e c a r 