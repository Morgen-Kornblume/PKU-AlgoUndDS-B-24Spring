# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getsum(self, low: int, high: int, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        ret = 0
        if root.val >= low and root.val <= high:
            ret += root.val
        ret += self.getsum(low, high, root.left)
        ret += self.getsum(low, high, root.right)
        return ret

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.getsum(low, high, root)
