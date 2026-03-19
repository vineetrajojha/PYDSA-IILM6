# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    #5 nodes, k = 2 then 2 rotations and effective rotations so that the same list doesn't appear twice or more.

    #step1: length of linked list
    def lenOfLL(self,head):
        l = 0
        cur = head
        while cur:
            cur  = cur.next
            l+=1
        return l
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None: return head
        n =self.lenOfLL(head)
        #step2 : divide by k and find remainder
        k=k%n
        if k ==0: return head
        jump = n - (k+1)
        cur = head
        while jump >0:
            cur = cur.next
            jump -= 1
        newHead = cur.next
        cur.next=None
        cur = newHead
        while cur.next:
            cur = cur.next
        cur.next = head
        return newHead
        
        

        
        



        