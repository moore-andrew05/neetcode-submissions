# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 or q2:
            if (q1 and not q2) or (q2 and not q1):
                return False

            node1 = q1.popleft()
            node2 = q2.popleft()

            if node1 and node2:
                if node1.val != node2.val:
                    return False
            
            if node1:
                if not node2:
                    return False
                q1.append(node1.left)
                q1.append(node1.right)
            
            if node2:
                if not node1:
                    return False
                q2.append(node2.left)
                q2.append(node2.right)

        return True