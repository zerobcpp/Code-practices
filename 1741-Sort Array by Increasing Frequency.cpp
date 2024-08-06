class Solution {
public:
    vector<int> frequencySort(vector<int>& nums) {
        map<int, int> c;
        for (auto i :nums){ 
            c[i]++;
        }
        priority_queue<pair<int, int>> st;
        vector<int> res;
        for(auto &[key, value] : c){
            st.push(pair<int, int>(-value, key));
        }
        while(!st.empty()){
            auto it = st.top();
            st.pop();
            //cout << it.first << it.second<<endl;
            for(int i = 0; i < -it.first; i++){
                res.push_back(it.second);
            }
        }
        return res;
    }
    
};

class compare{
    public:
    bool operator() (pair<int, int> a, pair<int, int> b){
        if(a.first == b.first)
            return a.second > b.second;
        return a.first > b.first;
    }
};