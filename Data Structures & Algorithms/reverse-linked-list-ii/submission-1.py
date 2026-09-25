# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftNode = start = dummy
        for _ in range(right):
            head = head.next
        rightNode = head
        for _ in range(left-1):
            leftNode = leftNode.next
            start = start.next
        start = start.next

        prev = rightNode
        while start != rightNode:
            tmp = start.next
            start.next = prev
            prev = start
            start = tmp
        
        leftNode.next = prev
        return dummy.next