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
    int res = INT_MAX;
    int minDepth(TreeNode* root) {
        helper(root, 1);
        return res;
    }
    void helper(TreeNode *node, int depth){
        if(node == NULL)
            return;
        if(!node->left && !node->right)
            res = min(res, depth);
        helper(node->left, depth+1);
        helper(node->right, depth+1);
    }
        
};