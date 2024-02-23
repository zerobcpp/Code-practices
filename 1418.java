class Solution {
    int ret = Integer.MAX_VALUE;
    public int distributeCookies(int[] cookies, int k) {
        helper(k, 0, cookies, new int[8]);
        return ret;
        
    }
    public void helper(int k, int cur, int[] arr, int[] plan){
        if(cur == arr.length){
            int mx = 0;
            for(int i : arr)
                mx = Math.max(mx, i);
            ret = Math.min(ret, mx);
            return;
        }
        for(int i = 0; i < k; i++){
            plan[cur] += arr[i];
            helper(k, cur + 1, arr, plan);
            plan[cur] -= arr[i];
        }
    }
}