class Solution {
    public long maximumHappinessSum(int[] happiness, int k) {
        Arrays.sort(happiness);
        //System.out.println(Arrays.toString(happiness));
        long res = 0;
        int n = happiness.length;
        for(int i = n -1; i > n - k - 1; i--){
            int rnds = n - i - 1;
            res += Math.max(happiness[i] - rnds, 0); 
        }
        return res;
    }
}