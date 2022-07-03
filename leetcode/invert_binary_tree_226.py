# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #52 ms
        # if not root:
        #     return None
        # root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        # return root
        #44 ms
        if not root:
            return None
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
