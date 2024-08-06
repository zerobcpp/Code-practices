public class Solution {
    public int ClimbStairs1(int n) {
        int p1 = 1;
        int p2 = 1;
        int cur = 0;
        for(int i = 2; i < n+1; i++){
            cur = p1 + p2;
            p1 = p2;
            p2 = cur;
        }
        return p2;
        
    }
    public int ClimbStairs(int n){
        int[] dp = new int[n+1];
        dp[0] = 1;
        dp[1] = 1;
        
        for(int i = 2; i < n+1; i++){
            dp[i] = dp[i-1] + dp[i-2];
        }
        return dp[n];
    }
}