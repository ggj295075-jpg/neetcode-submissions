# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def dfs(root, depth):
            if not root:
                return 
            res[depth].append(root.val) 
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)

        def maxDepth(root):
            if not root:
                return 0
            left = maxDepth(root.left)
            right = maxDepth(root.right)

            return 1 + max(left, right)
        
        localDepth = maxDepth(root)
        res = [[] for _ in range(localDepth)]

        dfs(root, 0)
        return res