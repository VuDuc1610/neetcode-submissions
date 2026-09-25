# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # curr = dummy = ListNode(0,head)
        # while head:
        #     if head.val != val:
        #         curr.next = head
        #         curr = curr.next
        #     head = head.next
        # curr.next = head
        # return dummy.next

        #another solution
        curr = dummy = ListNode(0, head)
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next