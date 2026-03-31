# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        last_node = None

        while node:
            print(node.val, node.next)

            tmp = node.next
            node.next = last_node
            last_node = node
            node = tmp


        return last_node