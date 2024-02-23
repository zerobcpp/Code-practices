class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        count = [1] * n
        
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
        
        print(length, count)
        max_length = max(length)
        result = 0
        
        for i in range(n):
            if length[i] == max_length:
                result += count[i]
        
        return result
    
    def findNumberOfLIS(self, nums: List[int]) -> int:
        subs = []
        d = defaultdict(list) 
        

        for num in nums:
            i = bisect.bisect_left(subs, num)
            if i == len(subs):
                subs.append(num)
            else:
                subs[i] = num
            count = 0
            for freq, end in d[i]:
                if end < num:
                    count += freq
            d[i+1].append([max(1, count), num])
        
        
        return sum(freq for freq, end in d[len(subs)])