class Solution {
public:
    vector<vector<int>> res;
    
    void helper(int i, vector<int>& nums){
            if(nums.size() == i)
                res.push_back(nums);
            
            for (int j = i; j < nums.size(); ++j){
                swap(nums[i], nums[j]);
                helper(i+1, nums);
                swap(nums[j], nums[i]);
            }
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        helper(0, nums);
        return res;
    }
};