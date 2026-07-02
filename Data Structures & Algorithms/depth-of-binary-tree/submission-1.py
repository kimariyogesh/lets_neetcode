# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # recursive approach
        # maximum depth for the end node = 1 => 1 + max(l, r)

        # base case 
        if root is None:
            return 0
        # recursive call 
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))                    

