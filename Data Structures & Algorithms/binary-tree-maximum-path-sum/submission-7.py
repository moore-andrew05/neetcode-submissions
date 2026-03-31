# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_path = None

        def dfs_with_path_sum(root):
            nonlocal max_path

            if not root:
                return 0
            
            left = dfs_with_path_sum(root.left)
            right = dfs_with_path_sum(root.right)



            if not root.left and not root.right:
                current_max_path = root.val
            elif not root.left:
                current_max_path = max(right, root.val + left + right, root.val)
            elif not root.right:
                current_max_path = max(left, root.val + left + right, root.val)
            else:
                current_max_path = max(left, right, root.val + left + right, root.val)
                
            if not max_path or current_max_path > max_path:
                max_path = current_max_path

            return root.val + max(0, left, right)

        root_max = dfs_with_path_sum(root)
        return max(max_path, root_max)


        
        