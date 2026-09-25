# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        l1 = self.reverse(l1)
        l2 = self.reverse(l2)
        carry = 0
        while l1 or l2 or carry:
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0

            num = num1 + num2 + carry 
            ans = ListNode(num%10, ans)
            carry = 0 if num < 10 else 1
            
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return ans

