class Solution:
    def sumSubarrayMins(self, nums: List[int]) -> int:
        N = len(nums)
        INF = 10 ** 5
        left = [-1] * N
        right = [N] * N
        MOD = 10 ** 9 + 7
        res = 0
        st = []
        for i, v in enumerate(nums):
            while st and nums[st[-1]] >= v:
                st.pop()
            if st:
                left[i] = st[-1]
            st.append(i)
        
        st = []
        for i in range(N - 1, -1, -1):
            while st and nums[st[-1]] > nums[i]:
                st.pop()
            if st:
                right[i] = st[-1]
            st.append(i)
        
        
        for i in range(N):
            res += (i - left[i]) * (right[i] - i) * nums[i]
            res %= MOD
        
        return res
            