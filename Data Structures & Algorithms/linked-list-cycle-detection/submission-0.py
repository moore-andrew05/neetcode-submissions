# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head

        while p1 and p2:
            p1 = p1.next

            try:
                p2 = p2.next.next
            except AttributeError:
                break

            if p1 is p2:
                return True

        return False