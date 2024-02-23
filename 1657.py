class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        N = len(arr)
        if k >= N:
            return max(arr)
        wins = 0
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
            
            #print(arr, cand, wins)
        
        return prev
    
    
    def getWinner(self, arr, k):
        n = len(arr)
        mx = max(arr)
        if k >= n:
            return max(arr)
        cand = arr[0]
        wins = 0
        for i in range(1, n):
            cmp = arr[i]
            if cand > cmp:
                wins += 1
            else:
                wins = 1
                cand = cmp
            
            
            if wins == k or cand == mx:
                return cand
            
            #print(cand, cmp, wins)
        return cand