class Solution {
public:
    long long maximumHappinessSum(vector<int>& happiness, int k) {
        sort(happiness.begin(), happiness.end());
        long long res = 0;
        int rounds = 0;
        int N = happiness.size();
        while(rounds < k && happiness.size() > 0){
            res += max(happiness.back()-rounds, 0);
            happiness.pop_back();
            rounds += 1;
        }
        return res;
        
    }
};