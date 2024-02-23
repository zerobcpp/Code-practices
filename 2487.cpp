class Solution {
public:
    int partitionString(string s) {
        int n = s.size();
        int res = 0;
        set<char> c;
        for (char i : s){
            if (c.find(i) != c.end()){
                res += 1;
                c.clear();
            }
            c.insert(i);
        }
        return res + 1;
    }
};