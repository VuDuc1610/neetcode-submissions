# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        if length <= 1 or k == 0 or k == length:
            return head
        k = k % length

        lead = lag = head
        for i in range(0,k):
            lead = lead.next
        while lead.next:
            lag = lag.next
            lead = lead.next
        
        ans = lag.next
        lag.next = None

        curr = ans
        while curr.next:
            curr = curr.next
        curr.next = head

        return ans