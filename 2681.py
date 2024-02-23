class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        if k == 1:
            return 0
        N = len(weights)
        bag = []
        for i in range(N-1):
            bag.append(weights[i] + weights[i+1])
        
        k -= 1
        #print(nlargest(k, bag), nsmallest(k, bag))
        return sum(nlargest(k, bag)) - sum(nsmallest(k, bag))
    
    def putMarbles(self, weights, k): 
        if k == 1:
            return 0
        N = len(weights)
        bag = []
        for i in range(N-1):
            bag.append(weights[i] + weights[i+1])
        bag.sort()
        k -= 1
        return sum(bag[-k:]) - sum(bag[:k])