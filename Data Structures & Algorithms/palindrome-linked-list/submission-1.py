# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(root):
            prev = None
            while root:
                tmp = root.next
                root.next = prev
                prev = root
                root = tmp
            return prev
        
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        temp = reverse(slow)

        while temp:
            if head.val != temp.val:
                return False
            head = head.next
            temp = temp.next

        return True