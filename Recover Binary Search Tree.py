# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def inorder(root, tree):
            if not root:
                return 
            if root.left:
                inorder(root.left, tree)
            tree.append(root.val)
            if root.right:
                inorder(root.right, tree)
            return tree
        
        def swapped(tree):
            x = y = -1
            for i in range(1, len(tree)):
                if tree[i - 1] > tree[i]:
                    y = tree[i]
                    if x == -1:
                        x = tree[i - 1]
                    else:
                        break
            return x, y
        
        def recover(r, count):
            if r:
                if r.val == x or r.val == y:
                    r.val = y if r.val == x else x
                    count -= 1
                    if count == 0:
                        return      
                recover(r.left, count)
                recover(r.right, count)
        
        nums = inorder(root, [])
        x, y = swapped(nums)
        recover(root, 2)
