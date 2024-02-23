class Solution {
public:
    int MOD = 1e9 + 7;
    
    int kInversePairs(int n, int k) {
        vector<vector<int>> dp(n+1, vector<int>(k+1, -1));
        return helper(dp, n, k);
    }
    int helper(vector<vector<int>>&dp, int n, int k){
        if(k <= 0)
            return k == 0 ? 1 : 0;
        if(dp[n][k] != -1)
            return dp[n][k];
        
        int cnt = 0;
        for(int i = 0; i < n; ++i){
            cnt += (helper(dp, n - 1, k - i) % MOD);
        }
        
        return dp[n][k] = cnt;
    }
};