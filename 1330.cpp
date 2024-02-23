class Solution {
public:
    map<pair<int, int>, int> dp;
    int longestSubsequence(vector<int>& arr, int difference) {
        return helper(arr, 0, INT_MIN, difference);
    }
    int helper(vector<int>& arr, int idx, int prev, int diff){
        if(idx >= arr.size())
            return 0;
        if (dp.count(make_pair(idx, prev)) != 0)
            return dp[(make_pair(idx, prev))];
        
        int nc = helper(arr, idx+1, prev, diff);
        int count = 0;
        if (prev + diff == arr[idx] || prev == INT_MIN) {
            count = max(1 + helper(arr, idx+1, arr[idx], diff), helper(arr, idx+1, prev, diff));
        }
        dp[make_pair(idx, prev)] = max(count, nc);
        return dp[make_pair(idx, prev)];
    }
};



//         self.res = 0
//         N = len(arr)
//         @cache
//         def helper(i, prev):
//             if i >= N:
//                 return 0
            
//             nc = helper(i+1, prev)
//             count = 0
//             if prev + difference == arr[i] or prev == -float('inf'):
//                 count = max(1 + helper(i+1, arr[i]), helper(i+1, prev))
            
            
//             return max(nc,count)
        
//         return helper(0, -float('inf'))