'''
    runtime: 243 ms Beats 41.39%
    memory: 23 MB Beats 86.6%
'''

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        range_sum = 0

        while stack:
            node = stack.pop()
            if node:
                if node.val > low:
                    stack.append(node.left)
                if low <= node.val <= high:
                    range_sum += node.val
                if node.val < high:
                    stack.append(node.right)

        return range_sum