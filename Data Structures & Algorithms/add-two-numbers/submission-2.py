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
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            sum = v1 + v2 + count
            if sum >= 10:
                count = 1
            else:
                count = 0
            
            temp.next = ListNode(sum % 10, None)
            temp = temp.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        if count == 1:
            temp.next = ListNode(1, None)

        return res.next
