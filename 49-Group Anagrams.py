class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = []
        count = 0
        while strs:
            inner = []
            for i in strs:
                for j in strs:
                    if sorted(i) == sorted(j):
                        inner.append(j)
                for deletes in inner:
                    strs.remove(deletes)
                break
            group.append(inner)
        return group