# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root is None:
            return 0
        
        stack = []
        stack.append(root)
        count_sum = 0

        while len(stack) > 0:
            cur = stack.pop()
            if cur.val >= L and cur.val <= R:
                count_sum += cur.val
            if cur.val > L and cur.left is not None:
                stack.append(cur.left)
            if cur.val < R and cur.right is not None:
                stack.append(cur.right)
        
        return count_sum
