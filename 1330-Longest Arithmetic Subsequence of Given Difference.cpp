class Solution {
public:
    
    int longestSubsequence(vector<int>& arr, int difference) {
        map<int, int> c;
        int res = 0;
        for(auto i : arr){
            int before = c[i-difference] ? c[i-difference] : 0;
            c[i] = ++before;
            res = max(res, c[i]);
        }
        // for (auto [first, second] : c){
        //     cout<< first<<second<<endl;
        // }
        return res;
    }
};



