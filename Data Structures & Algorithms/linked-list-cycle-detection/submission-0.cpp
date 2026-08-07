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
    bool hasCycle(ListNode* head) {
        set<ListNode*> a;
        ListNode *temp= head;
        while(temp){
            if(a.count(temp)){
                return true;
            }
            else{
                a.insert(temp);
            }
            temp=temp->next;
        }
        return false;
        
    }
};
