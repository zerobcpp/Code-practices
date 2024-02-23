class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        N = len(nums)
        st = deque()
        
        for i in range(k):
            while st and nums[i] >= nums[st[-1]]:
                st.pop()
            st.append(i)

        res.append(nums[st[0]])
        
        
        for i in range(k, N):
            while st and st[0] <= i - k:
                st.popleft()
            while st and nums[i] >= nums[st[-1]]:
                st.pop()
                
            st.append(i)
            res.append(nums[st[0]])
        
        
        return res     

    def maxSlidingWindow(self, nums, k):
        res = []
        N = len(nums)
        st = deque()
        for i in range(N):
            while st and st[0] <= i - k:
                st.popleft()
            while st and nums[i] >= nums[st[-1]]:
                st.pop()
                
            st.append(i)
            res.append(nums[st[0]])
        
        
        return res[k-1:]