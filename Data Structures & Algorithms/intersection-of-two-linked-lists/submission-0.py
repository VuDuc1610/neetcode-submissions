# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0,0
        tempA, tempB = headA, headB
        while tempA:
            lenA += 1
            tempA = tempA.next
        while tempB:
            lenB += 1
            tempB = tempB.next
        A, B = headA, headB
        if lenA > lenB:
            A, B = B, A
        
        #make sure A is always the shorter linkedList
        count = abs(lenA-lenB)
        while count > 0:
            B = B.next
            count -= 1

        # while A:
        #     print(A.val)
        #     A = A.next
        # print("#")
        # while B:
        #     print(B.val)
        #     B = B.next
        
        while A:
            if A == B:
                return A
            A = A.next
            B = B.next
        return None