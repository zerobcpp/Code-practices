class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set()
        deadends = set(deadends)
        st = deque(['0000'])
        level = 0 
        while st:
            
            n = len(st)
            for _ in range(n):
                cur = st.popleft()
                if cur in deadends:
                    continue
                if cur == target:
                    return level
                
                for i in range(4):
                    
                    for digit in [-1, 1]:
                        temp = list(cur)
                        temp[i] = str((int(temp[i]) + digit) % 10)
                        temp = ''.join(temp)
                        if temp not in seen:
                            seen.add(temp)
                            st.append(temp)
            level += 1
        
        return -1
        