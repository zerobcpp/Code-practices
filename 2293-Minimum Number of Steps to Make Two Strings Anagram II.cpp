class Solution {
public:
    int minSteps(string s, string t) {
        int c[26] = {0};
        
        for (char i : s)
            c[i-'a'] += 1;
        
        for (char i : t)
            c[i-'a'] -= 1;
        
        int res = 0;
        for(int i = 0; i < 26; i++){
            res += abs(c[i]);
        }
        return res;
    }
};