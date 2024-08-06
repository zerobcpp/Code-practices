class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int cur = 0, res = INT_MIN;
        
        for(int i : nums){
            cur = max(i, cur + i);
            res = max(res, cur);
        }
        return res;
    }
};