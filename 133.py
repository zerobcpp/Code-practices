# 133. Clone Graph
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        c = {}
        c[node] = Node(node.val)
        st = [node]
        while st:
            cur = st.pop()

            for neigh in cur.neighbors:
                if neigh not in c:
                    st.append(neigh)
                    c[neigh] = Node(neigh.val)
                c[cur].neighbors.append(c[neigh])

        return c[node]