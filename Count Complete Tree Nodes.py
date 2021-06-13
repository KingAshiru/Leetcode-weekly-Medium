from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque()
        queue.append(root)
        count = 1
        
        while queue:
            for _ in range(len(queue)):
                node = queue.pop()
                if node.left:
                    queue.appendleft(node.left)
                    count += 1
                if node.right:
                    queue.appendleft(node.right)
                    count += 1
        return count
