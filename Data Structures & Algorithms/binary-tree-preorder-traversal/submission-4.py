# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []

        def dfs(root, array):
            if not root:
                return 
            
            array.append(root.val)
            dfs(root.left, array)
            dfs(root.right, array)
        dfs(root, l)
        return l