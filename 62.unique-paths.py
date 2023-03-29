#
# @lc app=leetcode id=62 lang=python3
#
# [62] Unique Paths
#

# @lc code=start
from math import comb
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        d = m + n
        return comb(m, d)
        
# @lc code=end

