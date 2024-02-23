class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums:
            return None
        n = {}
        
        for i in nums:
            n[i] = n.get(i, 0) + 1
        
        # get k elements only
        nSorted = sorted(n.items(), key = operator.itemgetter(1), reverse = True)
        
        return [i for i,v in nSorted[:k:]]
        