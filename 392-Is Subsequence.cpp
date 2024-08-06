class Solution {
public:
    bool isSubsequence(string s, string t) {
        int ns = s.size();
        int nt = t.size();
        int i = 0, j = 0;
        
        while (i < ns && j < nt){
            if (s.at(i) == t.at(j))
                i++;
            j++;
        }
        return i == ns;
    }
};