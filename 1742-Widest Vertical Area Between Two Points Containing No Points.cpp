class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        sort(points.begin(), points.end());
        int n = points.size();
        int res = 0;
        for(int i = 1; i < n; i++){
            int x = points[i-1][0];
            int dx = points[i][0];
            res = max(res, dx - x);
        }
        return res;
    }
};