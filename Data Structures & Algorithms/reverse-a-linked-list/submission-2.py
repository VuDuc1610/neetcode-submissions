# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, tmp = None, head

        while tmp:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
        
        return prev