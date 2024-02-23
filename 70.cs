public class Solution {
    public int ClimbStairs(int n) {
        int p1 = 1;
        int p2 = 1;
        int cur = 0;
        for(int i = 2; i < n+1; i++){
            cur = p1 + p2;
            p1 = p2;
            p2 = cur;
        }
        return cur;
        
    }
}