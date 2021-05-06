# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        idx = {}
        for i, val in enumerate(inorder):
            idx[val] = i
        
        stack = []
        head = None
        
        for val in postorder[::-1]:
            if not head:
                head = TreeNode(val)
                stack.append(head)
            else:
                node = TreeNode(val)
                if idx[val] > idx[stack[-1].val]:
                    stack[-1].right = node
                else:
                    while stack and idx[val] < idx[stack[-1].val]:
                        u = stack.pop()
                    u.left = node
                stack.append(node)
        return head
