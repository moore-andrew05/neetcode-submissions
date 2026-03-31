# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.max_depth = 0

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode], depth: int):
            if not root:
                return None

            if depth > self.max_depth:
                self.max_depth = depth

            dfs(root.left, depth + 1)
            dfs(root.right, depth + 1)


        dfs(root, 1)

        return self.max_depth