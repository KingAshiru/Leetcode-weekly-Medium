from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        maxWidth = 0
        q = deque([(root, 0)])
        
        while q:
            l = q[0][1]
            size = len(q)
            for _ in range(size):
                node, index = q.popleft()
                if node.left:
                    q.append((node.left, 2 * index + 1))
                if node.right:
                    q.append((node.right, 2 * index + 2))
            
            maxWidth = max(maxWidth, index - l + 1)
            
        return maxWidth
