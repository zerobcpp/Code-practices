class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        if nums[-1] == 1:
            nums = [1] + nums[:-1]
        pf = []
        n = len(nums)
        print(nums)
        r = 0
        while r < n:
            advance = False
            if nums[r] == 1:
                advance = True
                cnt = 0
                l = r
                while l < n and nums[l] == 1:
                    l += 1
                    cnt += 1
            
                pf.append(cnt)
            
            if advance:
                r = l + 1
            else:
                r += 1
                
        heapify(pf)
        res = 0
        while len(pf) > 1:
            swap = heappop(pf)
            bind = heappop(pf)
            heappush(pf, swap + bind)
            res += swap
        
        return res
    
    
    def minSwaps(self, nums):
        N = len(nums)
        def helper(element):
            cnt = 0
            for i in nums:
                if i == element:
                    cnt += 1
            if N == cnt or cnt == 0:
                return 0
            fin_window = 0
            cur_window = 0
            for r in range(cnt):
                if nums[r] == element:
                    cur_window += 1
            
            fin_window = cur_window
            l = 0
            r += 1
            while r < N:
                if nums[l] == element:
                    cur_window -= 1
                l += 1
                if nums[r] == element:
                    cur_window += 1
                r += 1
                fin_window = max(cur_window, fin_window)
                # if element == 0:
                #     print(fin_window)
            
            return cnt - fin_window
        
        one = helper(1)
        zero = helper(0)
        #print(one, zero)
        return min(one, zero)
                    