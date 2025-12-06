class FenwickTree:
    def __init__(self, x):
        """transform list into BIT"""
        self.bit = x
        for i in range(len(x)):
            j = i | (i + 1)
            if j < len(x):
                x[j] += x[i]

    def update(self, idx, x):
        """updates bit[idx] += x"""
        while idx < len(self.bit):
            self.bit[idx] += x
            idx |= idx + 1

    def query(self, end):
        """calc sum(bit[:end])"""
        x = 0
        while end:
            x += self.bit[end - 1]
            end &= end - 1
        return x

    def findkth(self, k):
        """Find largest idx such that sum(bit[:idx]) <= k"""
        idx = -1
        for d in reversed(range(len(self.bit).bit_length())):
            right_idx = idx + (1 << d)
            if right_idx < len(self.bit) and k >= self.bit[right_idx]:
                idx = right_idx
                k -= self.bit[idx]
        return idx + 1
        
    def __str__(self):
        return f"{self.bit}"
            
    
    
class FenwickP():
    
    def __init__(self, N):
        self.tree = [0] * (N+1) 
    
    def make(self, arr):
        N = len(arr)
        self.tree = arr
        for i in range(N):
            j = i | (i + 1)
            if j < N:
                arr[j] += arr[i]
        
    
    def pfsum(self, i):
        sm = 0
        while i != 0:
            sm += self.tree[i]
            i = i & -i
        return sm
    
    def query_range(self, i, j):
        return self.pfsum(j) - self.pfsum(i-1)
    
    def add(self, i, val):
        while i < len(self.tree):
            self.tree[i] += val
            i = i + (i & -i)
    
    def update(self, i, val):
        k = self.query_range(i, i)
        self.add(i, val - k)
        

    def __str__(self):
        return self.tree
    

