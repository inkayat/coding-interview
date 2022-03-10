/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
 struct ListNode*  listnode_new(int val) {
    struct ListNode*  node = (struct ListNode* ) malloc(sizeof(struct ListNode ));
     node->val = val;
     node->next = NULL;
     return node;
  }

 struct ListNode* addTwoNumbers(struct ListNode* A, struct ListNode* B) {
    int carry=0;
    struct ListNode* head=NULL, *prev;
    while (A || B || carry) {
        int val;
        val = carry;
        if (A) {
            val += A->val;
            A = A->next;
        }
        if (B) {
            val += B->val;
            B = B->next;
        }
        if (val > 9) {
            val -= 10;
            carry = 1;
        } else {
           carry = 0;
        }
        struct ListNode *n = listnode_new(val);
        if (!head) {
            head = n;
            prev = head;
        } else {
            prev->next = n;
            prev = n;
        }
    }
    return head;
} 
