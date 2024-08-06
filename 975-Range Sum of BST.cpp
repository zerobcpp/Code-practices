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
    int rangeSumBST1(TreeNode* root, int low, int high) {
        helper(root, low, high);
        return res;
    }
    
    int rangeSumBST(TreeNode *root, int low, int high){
        int res = 0;
        stack<TreeNode> c;
        c.push(*root);
        
        while(!c.empty()){
            TreeNode cur = c.top();
            c.pop();
            if (cur.val >= low && cur.val <= high){
                res += cur.val;
            }
            if(cur.left)
                c.push(*cur.left);
            if (cur.right)
                c.push(*cur.right);
        }
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