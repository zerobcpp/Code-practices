class Solution {
public:
    int countSeniors(vector<string>& details) {
        int res = 0;
        for (auto s : details){
            string temp = s.substr(11, 2);
            int c = stoi(temp);
            if (c > 60) ++res;
            
        }
        
        return res;
    }
};