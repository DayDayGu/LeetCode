# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: 'TreeNode', k: 'int') -> 'int':
        count = 0
        stack = []
        stack.append(root)

        while len(stack) != 0:
            cur_node = stack.pop()
            if cur_node.left is not None:
                cur_left = cur_node.left
                cur_node.left = None
                stack.append(cur_node)
                stack.append(cur_left)
                continue
            
            count += 1
            if count == k:
                return cur_node.val
            
            if cur_node.right is not None:
                stack.append(cur_node.right)
