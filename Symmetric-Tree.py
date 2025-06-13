# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        \\\
        :type root: Optional[TreeNode]
        :rtype: bool
        \\\
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    def isMirror(self,p,q):
        if p is None and q is None:
            return True
        if (p is None)!=(q is None):
            return False
        if p.val!=q.val:
            return False
        return self.isMirror (p.left,q.right) and self.isMirror (p.right,q.left)