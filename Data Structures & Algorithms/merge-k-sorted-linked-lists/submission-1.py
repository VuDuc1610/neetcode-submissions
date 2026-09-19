# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def merge2Lists(self, list1, list2):
        head = ListNode()
        res = head
        while list1 and list2:
            if list1.val >= list2.val:
                head.next = list2
                list2 = list2.next
            else:
                head.next = list1
                list1 = list1.next
            head = head.next
        if list1:
            head.next = list1
        else:
            head.next = list2
        return res.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: 
            return None
        count = 0
        merged = []
        while True:
            if count == len(lists):
                count = 0
                lists = merged
                merged = []
            elif count == len(lists)-1:
                merged.append(lists[count])
                count = 0
                lists = merged
                merged = []
            if len(lists) == 1:
                return lists[0]
            temp = self.merge2Lists(lists[count], lists[count+1])
            merged.append(temp)
            count += 2
        return 