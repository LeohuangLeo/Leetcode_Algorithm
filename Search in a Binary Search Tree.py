#700
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        elif root.val > val:
            root = root.left
            return self.searchBST(root, val)
        elif root.val < val:
            root = root.right
            return self.searchBST(root, val)

