# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev, curr = None, slow
        while curr:
            curr = curr.next
            slow.next = prev
            prev = slow
            slow = curr

        while prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True