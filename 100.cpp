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
    bool isSameTree(TreeNode* p, TreeNode* q) {
            std::stack<TreeNode*> st;
            st.push(p);
            st.push(q);

            while (!st.empty()) {
                TreeNode* cur_q = st.top();
                st.pop();
                TreeNode* cur_p = st.top();
                st.pop();

                if (!cur_p && !cur_q)
                    continue;
                if (!cur_p || !cur_q || cur_p->val != cur_q->val)
                    return false;

                st.push(cur_p->left);
                st.push(cur_q->left);
                st.push(cur_p->right);
                st.push(cur_q->right);
            }

            return true;
    }
};