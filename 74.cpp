class Solution {
public:
    bool searchMatrix1(vector<vector<int>>& matrix, int target) {
        for (auto i : matrix){
            for(auto j : i){
                if(j==target)
                    return true;
            }
        }
        return false;
    }
     bool searchMatrix(vector<vector<int>>& matrix, int target) {
         int n = matrix.size();
         int m = matrix[0].size();
         int l = 0, r = n * m - 1;
         while(l <= r){
             int mid = l + (r - l) / 2;
             int i = mid / m;
             int j = mid % m;
             if (matrix[i][j] == target)
                 return true;
             if (matrix[i][j] > target)
                 r = mid - 1;
             else
                 l = mid + 1;
             
         }
         return false;
     }
};