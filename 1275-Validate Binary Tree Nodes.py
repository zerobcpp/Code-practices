class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        graph = {i : [] for i in range(n)}
        
        
        for i, (lc, rc) in enumerate(zip(leftChild, rightChild)):
            if lc != -1:
                graph[lc].append(i)
            if rc != -1:
                graph[rc].append(i)
        
        st = []
        for i, v in graph.items():
            if graph[i] == []:
                st.append(i)
                break
        seen = set(st)
        while st:
            cur = st.pop()
            
            for neigh in [leftChild[cur], rightChild[cur]]:
                if neigh in seen:
                    return False
                elif neigh not in seen and neigh != -1:
                    seen.add(neigh)
                    st.append(neigh)
        
        
        return len(seen) == n
                        
        
        