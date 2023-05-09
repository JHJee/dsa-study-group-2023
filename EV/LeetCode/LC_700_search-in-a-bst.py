'''
    runtime: 73 ms Beats 85.97%
    memory: 16.4 MB Beats 57.64%
'''

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if val == root.val:
            return root
        elif val < root.val and root.left:
            return self.searchBST(root.left, val)
        elif val > root.val and root.right:
            return self.searchBST(root.right, val)
        else:
            return None