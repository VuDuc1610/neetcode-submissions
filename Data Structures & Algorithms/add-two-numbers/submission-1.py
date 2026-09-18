# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        temp = res
        count = 0

        while l1 or l2:
            sum = 0
            if not l1:
                sum = l2.val + count
                l2 = l2.next
            elif not l2:
                sum = l1.val + count
                l1 = l1.next
            else:
                sum = l1.val + l2.val + count
                l1 = l1.next
                l2 = l2.next
            if sum >= 10:
                count = 1
            else:
                count = 0
            
            temp.next = ListNode(sum % 10, None)
            temp = temp.next
        if count == 1:
            temp.next = ListNode(1, None)

        return res.next
