from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        
        queue = deque()
        queue.append(root)
        result = []
        leftToRight = True
        
        while queue:
            length = len(queue)
            level = deque()
            
            for _ in range(length):
                node = queue.popleft()
                if leftToRight:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
            leftToRight = not leftToRight
            
        return result
