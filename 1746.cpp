class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        unordered_map<char, int> c;
        int res = -1;
        
        for(int i = 0; i < s.size(); i++){
            if(c.find(s[i]) != c.end())
                res = max(res, i - c[s[i]]- 1);
            else
                c[s[i]] = i;
        }
        return res;
    }
};