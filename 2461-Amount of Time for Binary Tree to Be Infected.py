# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        st = [(root, None)]
        graph = defaultdict(list)
        while st:
            cur, parent = st.pop()
            if parent:
                graph[cur.val].append(parent.val)
                graph[parent.val].append(cur.val)
            for child in [cur.left, cur.right]:
                if child:
                    st.append((child, cur))
        #print(graph)
                
        
#         def helper(node):
#             if not node:
#                 return
#             cur = node.val
#             if node.left:
#                 left = node.left.val
#                 graph[cur].append(left)
#                 graph[left].append(cur)
#             if node.right:
#                 right = node.right.val
#                 graph[cur].append(right)
#                 graph[right].append(cur)
            
#             helper(node.left)
#             helper(node.right)
            
        #helper(root)
        #print(graph)
        seen = set()
        seen.add(start)
        st = deque([(start, 0)])
        res = 0
        while st:
            cur, level = st.popleft()
            res = level
            
            for neigh in graph[cur]:
                if neigh not in seen:
                    seen.add(neigh)
                    st.append((neigh, level + 1))

        return res