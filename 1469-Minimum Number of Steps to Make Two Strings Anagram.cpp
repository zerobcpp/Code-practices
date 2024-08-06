class Solution {
public:
    int minSteps(string s, string t) {
        unordered_map<char, int> c;
        
        for(char i : s)
            c[i] += 1;
        for (char i : t)
            c[i] -= 1;
        
        int res = 0;
        for(auto &it : c){
            res += max(0, it.second);
        }
        
        return res;
    }
};