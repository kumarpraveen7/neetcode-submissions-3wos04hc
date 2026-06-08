# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if(head == None or head.next == None):
            return False
        curr = head
        prev = head
        while(curr!=None and curr.next!=None):
            curr = curr.next.next
            prev = prev.next
            if(curr==prev):
                return True
        return False

        