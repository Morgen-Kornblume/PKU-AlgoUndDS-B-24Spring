# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)

        if len(preorder) == 1:
            return root

        left_val = preorder[1]
        left_index = postorder.index(left_val)

        root.left = self.constructFromPrePost(preorder[1:left_index+2], postorder[:left_index+1])
        root.right = self.constructFromPrePost(preorder[left_index+2:], postorder[left_index+1:-1])

        return root