class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {
        unordered_map<string, int> c;
        int cur = 0;
        for(auto s : arr)
            c[s] += 1;
        
        for (auto v : arr){
            if (c[v]==1){
                cur += 1;
                if (cur==k)
                    return v;
            }
        }
        return "";
    }
};