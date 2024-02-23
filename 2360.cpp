class Solution {
public:
    int largestVariance(string s) {
        map<char, int> c;
        for(char i : s){
            c[i] += 1;
        }
        
        int res = 0;
        for (auto &i : c){
            for (auto [j, v2] : c){
                if (i.first == j)
                    continue;
                int diff = 0;
                bool isJ = false;
                int jcnt = v2;
                for (char k : s){
                    if(k != i.first and k != j)
                        continue;
                    if (k == i.first)
                        diff ++;
                    else if (k == j){
                        diff --;
                        jcnt --;
                        isJ = true;
                        if (diff < 0 && jcnt > 0){
                            isJ = false;
                            diff = 0;
                        }
                    }
                    //cout << i.first << j << diff << endl;
                    if(isJ)
                        res = max(res, diff);
                }
            }
        }
        
        return res;
    }
};



// class Solution:
//     def largestVariance(self, s: str) -> int:
//         res = 0
//         c = Counter(s)
//         seen = set()
//         res = 0
//         for i in s:
//             for j in s:
//                 if i == j:
//                     continue
                
//                 diff = 0
//                 isJ = False
//                 jcnt = c[j]
//                 for k in s:
//                     if k == i:
//                         diff += 1
//                     elif k == j:
//                         diff -= 1
//                         isJ = True
//                         jcnt -= 1
//                         if diff < 0 and jcnt > 0:
//                             diff = 0
//                             isJ = False
//                     if isJ:
//                         res = max(res, diff)

//         return res