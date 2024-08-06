class Solution {
public:
    int bagOfTokensScore(vector<int>& tokens, int power) {
        sort(tokens.begin(),tokens.end());
        int n = tokens.size();
        int l = 0, r = n - 1;
        int res = 0;
        int cnt = 0;

        while(l <= r){
            if (power >= tokens[l]){
                power -= tokens[l];
                cnt ++;
                l ++;
            }
            else if(l < r && cnt > 0){
                power += tokens[r];
                r--;cnt--;
            }
            else{
                break;
            }
            
            res = max(res, cnt);
        }
        return res;
    }
};