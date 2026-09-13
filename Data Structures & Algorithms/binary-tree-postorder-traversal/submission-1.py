# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        leftArray = []
        rightArray = []

        def dfs(root, array):
            if not root:
                return
            dfs(root.left, array)
            dfs(root.right, array)
            array.append(root.val)
        dfs(root.left, leftArray)
        dfs(root.right, rightArray)
        return leftArray + rightArray + [root.val]