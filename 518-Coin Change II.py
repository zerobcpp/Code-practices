class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
       # print(dp)
        
        for c in coins:
            for i in range(c, amount+1):
                dp[i] += dp[i-c]
            print(dp)
        
        return dp[-1]
    
    def change(self, amount, coin):
        N = len(coin)
        
        @cache
        def helper(i, left):
            if left == 0:
                return 1
            if i >= N:
                return 0

            #count = 0
            if coin[i] > left:
                return helper(i+1, left)
            else:
                return helper(i, left - coin[i]) + helper(i+1, left)
            
        
        return helper(0, amount)
            
        
    