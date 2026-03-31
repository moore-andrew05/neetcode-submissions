# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        good_nodes = 1

        def dfs(root, max_in_path):
            nonlocal good_nodes
            if not root:
                return
            
            if root.val >= max_in_path:
                good_nodes += 1
                max_in_path = root.val

            dfs(root.left, max_in_path)
            dfs(root.right, max_in_path)

        dfs(root.left, root.val)
        dfs(root.right, root.val)

        return good_nodes
