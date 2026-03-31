# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    DELIM = ';'
    NULL_INDICATOR = 'X'
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        q = deque([root])
        ser = ""
        num_null = 0

        while q:
            node = q.popleft()
            if not node:
                num_null += 1
                continue

            if num_null > 0:
                ser += self.NULL_INDICATOR + str(num_null) + self.DELIM
                num_null = 0
            
            ser += str(node.val) + self.DELIM
            q.append(node.left)
            q.append(node.right)
        print(ser) 
        return ser[:-1]
            


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = deque(data.split(';'))
        root = TreeNode(val=data.popleft())
        q = deque([root]) 

        def processNull(data):
            num_null = int(data.popleft()[1:])
            for _ in range(num_null):
                data.appendleft(None)

            return data

        while q:
            node = q.popleft()
            if not node:
                continue

            

            lr = []
            for _ in range(2):
                if data:
                    if data[0] and data[0][0] == 'X':
                        data = processNull(data)

                    tmp = data.popleft()
                    if tmp:
                        tmp = int(tmp)
                    
                    lr.append(tmp)

            if len(lr) > 0:
                left = TreeNode(val = lr[0]) if lr[0] else None
                node.left = left
                q.append(left)

            if len(lr) > 1:
                right = TreeNode(val = lr[1]) if lr[1] else None
                node.right = right
                q.append(right)
        
        return root
