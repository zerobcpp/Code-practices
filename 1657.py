class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        wins = 1
        arr = deque(arr)
        cand = None
        prev = None
        while wins != k:
            x, y = arr.popleft(), arr.popleft()
            
            if x > y:
                cand = x
                arr.appendleft(x)
                arr.append(y)
            else:
                cand = y
                arr.appendleft(y)
                arr.append(x)
            
            
            if prev == cand:
                wins += 1
            else:
                wins = 1
            prev = cand
            
            #rint(arr, cand, wins)
        
        return prev