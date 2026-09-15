# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l,curr = None, head
        while curr:
            curr = curr.next
            head.next = l
            l = head
            head = curr
        return l