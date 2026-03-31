# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False


        def check_subtree(root, subroot):
            if not root and not subroot:
                return True
            
            if root and subroot and root.val == subroot.val:
                return check_subtree(root.left, subroot.left) and check_subtree(root.right, subroot.right)
            else:
                return False

        q = deque([root])

        while q:
            node = q.popleft()
            if not node:
                continue
            
            if node.val == subRoot.val and check_subtree(node, subRoot):
                return True

            q.append(node.left)
            q.append(node.right)
    
        return False


            
