# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if(head==None):
            return
        curr = head
        prev = head
        temp = head
        while(n>0):
            n-=1
            curr = curr.next
        if(curr==None):
            print(head.val)
            curr = head
            head = curr.next
            curr = head
            if(curr!=None):
                print(curr.val)
            
            return head

        while(curr!=None):
            curr = curr.next
            temp = prev
            prev = prev.next
        temp.next = prev.next
        return head
        