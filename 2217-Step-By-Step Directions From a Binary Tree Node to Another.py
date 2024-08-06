# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parent = {}
        st = [root]
        mode = {1: 'L', 2: 'R', 3: 'U'}
        while st:
            cur = st.pop()
            
            if cur.left:
                parent[cur.left.val] = cur
                st.append(cur.left)
            if cur.right:
                parent[cur.right.val] = cur
                st.append(cur.right)
        
        st = [root]
        start = None
        while st:
            cur = st.pop()
            if cur.val == startValue:
                start = cur
                break
            for child in [cur.left, cur.right]:
                if child:
                    st.append(child)
        
        st = deque([[start, '']])
        seen = set([start.val])
        while st:
            cur, ret = st.popleft()
            #print(cur.val)
            if cur.val == destValue:
                return ret
            i = 1
            for routes in [cur.left, cur.right, parent.get(cur.val, None)]:
                if routes and routes.val not in seen:
                    st.append([routes, ret + mode[i]])
                    seen.add(routes.val)
                i += 1
            #print(st)
        
        return None
    
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        parent = {}
        st = [root]
        mode = {1: 'L', 2: 'R', 3: 'U'}
        while st:
            cur = st.pop()
            
            if cur.left:
                parent[cur.left.val] = cur
                st.append(cur.left)
            if cur.right:
                parent[cur.right.val] = cur
                st.append(cur.right)
        
        st = [root]
        start = None
        while st:
            cur = st.pop()
            if cur.val == startValue:
                start = cur
                break
            for child in [cur.left, cur.right]:
                if child:
                    st.append(child)
        
        st = deque([[start, []]])
        seen = set([start.val])
        while st:
            cur, ret = st.popleft()
            #print(cur.val)
            if cur.val == destValue:
                return ''.join(ret)
            i = 1
            for routes in [cur.left, cur.right, parent.get(cur.val, None)]:
                if routes and routes.val not in seen:
                    ret.append(mode[i])
                    st.append([routes, ret.copy()]) 
                    seen.add(routes.val)
                i += 1
            #print(st)
        
        return None
    
    
    def getDirections(self, root, start, end):
        
        def findCommonP(node):
            if not node:
                return None
            if node.val == start or node.val == end:
                return node
            left = findCommonP(node.left)
            right = findCommonP(node.right)
            if left and right:
                return node
            
            return left if left else right
        
        parent = findCommonP(root)
        
        def helper(node, dest, route):
            if not node:
                return None
            if node.val == dest:
                return True
            route.append('L')
            if helper(node.left, dest, route):
                return True
            route.pop()
            route.append('R')
            if helper(node.right, dest, route):
                return True
            route.pop()
            return False
        
        route_start = []
        route_end = []
        helper(parent, start, route_start)
        helper(parent, end, route_end)
        
        return ''.join([len(route_start) * 'U'] + route_end)
            
        
                