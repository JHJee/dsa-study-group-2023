'''
    runtime: 34 ms Beats 58.63%
    memory: 13.7 MB Beats 96.36%
'''
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return False
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if not left:
                node.left = None
            if not right:
                node.right = None
            return node.val == 1 or left or right

        return root if dfs(root) else None
