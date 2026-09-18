# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        start = ListNode()
        start.next = head
        res = start
        lag, lead = start, start
        while n > 0:
            lead = lead.next
            n -= 1
        
        while lead:
            lead = lead.next
            lag = lag.next
        
        while start:
            if start.next == lag:
                start.next = lag.next
            start = start.next
        
        return res.next
