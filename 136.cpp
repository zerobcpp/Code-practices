class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> c;
        
        for(int i : nums){
            c[i] += 1;
        }
        
        for (auto &it : c){
            if(it.second == 1)
                return it.first;
        }
        return -1;
    }
};