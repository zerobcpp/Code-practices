/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        string s1, s2;
        
        while (l1){
            s1 += to_string(l1->val);
            l1 = l1->next; 
        }
        while (l2){
            s2 += to_string(l2->val);
            l2 = l2->next;
        }
        int x = stoi(s1) + stoi(s2);
        string s3 = to_string(x);
        ListNode *dummy = new ListNode(-1);
        ListNode *cur = dummy;
        
        for(int i = 0; i < s3.size(); i++){
            int val = int(s3[i] - '0');
            cur->next = new ListNode(val);
            //cout<<cur->val<<endl;; 
            cur = cur->next;
        }
        
        return dummy->next;
    }
};