# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def flatten(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        \\\
        self.prev= None
        def preorder(node):
            if not node:
                return
            preorder(node.right)
            preorder(node.left)
            node.left=None
            node.right=self.prev
            self.prev=node

        preorder(root)


