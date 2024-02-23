class Solution {
public:
    int climbStairs1(int n) {
        int dp [n+1];
        dp[0] = 1, dp[1] = 1;

        for(int i = 2; i < n+1; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];

    }
    
    int climbStairs(int n){
        int p1 = 1, p2 = 1;
        int cur = 0;
        for(int i = 2; i < n+1; i++){
            cur = p1 + p2;
            p1 = p2;
            p2 = cur;
        }
        return p2;
    }
};


/*
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

*/