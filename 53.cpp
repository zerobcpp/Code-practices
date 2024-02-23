class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int cur = 0, res = 0;
        
        for(int i : nums){
            cur = max(i, cur + i);
            res = max(res, cur);
        }
        return res;
    }
};