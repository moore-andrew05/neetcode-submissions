# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stk = deque([root])

        def find_node_path(root, target) -> List[str]:
            path = deque([])
            while root:
                if root.val > target:
                    root = root.left
                    path.append("L")
                elif root.val < target:
                    root = root.right
                    path.append("R")
                else:
                    return path

        pathp = find_node_path(root, p.val)
        pathq = find_node_path(root, q.val)

        while pathp and pathq:
            d1 = pathp.popleft()
            d2 = pathq.popleft()

            if d1 != d2:
                return root

            if d1 == "L":
                root = root.left
            else:
                root = root.right

        return root




