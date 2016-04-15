/*
 *   Reverse a linked list and return pointer to the head
 *   The input list will have at least one element  
 *   Node is defined as 
 *   struct Node
 *   {
 *       int data;
 *       struct Node *next;
 *   }
 *  
 */
Node* Reverse(Node *head)
{
    Node* prev = NULL;
    Node* next = NULL;
    Node* curr = head;
    while (curr) {        
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    return prev;
}

