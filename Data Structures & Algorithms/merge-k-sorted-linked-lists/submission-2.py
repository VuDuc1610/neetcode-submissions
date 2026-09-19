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
        
        while len(lists) > 1:
            merged = []
            for i in range(0,len(lists), 2):
                list1 = lists[i]
                list2 = lists[i + 1] if i < len(lists) - 1 else None
                temp = self.merge2Lists(list1, list2)
                merged.append(temp)
            lists = merged
        return lists[0] 