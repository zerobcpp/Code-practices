/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int res = 0;
    int rangeSumBST(TreeNode* root, int low, int high) {
        helper(root, low, high);
        return res;
    }
    void helper (TreeNode *node, int l, int h){
            if (!node)
                return;
            if (node->val >= l && node->val <= h){
                res += node->val;
            }
            helper(node->left, l, h);
            helper(node->right, l, h);
    }
        
        
};