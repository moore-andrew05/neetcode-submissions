# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        
        if not list2 and list1:
            return list1

        if not list2 and not list2:
            return None
        
            

        head = list1 if list1.val <= list2.val else list2

        prev = None

        while list1 and list2:
            if not prev:
                if list1.val <= list2.val:
                    prev = list1
                    list1 = list1.next
                else:
                    prev = list2
                    list2 = list2.next
                continue

            if list1.val <= list2.val:
                prev.next = list1
                prev = list1
                list1 = list1.next

            else:
                prev.next = list2
                prev = list2
                list2 = list2.next

        rem = None
        if list1:
            rem = list1
        elif list2:
            rem = list2

        while rem:
            prev.next = rem
            prev = rem
            rem = rem.next

        return head
