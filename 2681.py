class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        N = len(weights)
        bag = []
        for i in range(N-1):
            bag.append(weights[i] + weights[i+1])
        
        
        print(nlargest(k, bag), nsmallest(k, bag))
        
        return sum(nlargest(k, bag)) - sum(nsmallest(k, bag))