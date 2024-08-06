class Solution:
    def isNStraightHand(self, hand: List[int], k: int) -> bool:
        n = len(hand)
        if n % k != 0:
            return False
        res = []
        
        c = defaultdict(int)
        for i in hand:
            c[i] += 1
        
        st = list(c.keys())
        heapify(st)
        while st:
            cur = st[0]
            temp = []
            for i in range(cur, cur + k):
                if i not in c or c[i] < 0:
                    return False
                temp.append(i)
                c[i] -= 1
                if c[i] == 0:
                    x = heappop(st)
                    if x != i:
                        return False
            
            res.append(temp)
        
        return all(len(i) == k for i in res)