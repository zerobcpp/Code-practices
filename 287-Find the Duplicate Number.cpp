class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        set<int> c;
        for(int i : nums){
            if(c.find(i) != c.end())
                return i;
            c.insert(i);
        }        
        return -1;
    }
};