# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, low, high):

            # exit condition
            if not node:
                return True

            # node must be within the allowed range
            if node.val <= low or node.val >= high:
                return False

            # check left and right subtree
            isval = dfs(node.left, low, node.val) and \
                    dfs(node.right, node.val, high)

            return isval

        return dfs(root, float("-inf"), float("inf"))