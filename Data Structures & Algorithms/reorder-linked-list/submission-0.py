# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow,fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next

        prev = slow.next = None
        pos = second
        while pos:
            pos = pos.next
            second.next = prev
            prev = second
            second = pos
        
        while prev:
            temp1, temp2 = prev.next, head.next
            head.next = prev
            prev.next = temp2
            head = temp2
            prev = temp1
        
        