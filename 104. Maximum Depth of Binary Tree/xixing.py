# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if root is None:
            return depth
        current_layer = []
        next_layer = [root]
        while len(next_layer) > 0:
            depth += 1
            current_layer = next_layer
            next_layer = []
            for node in current_layer:
                if node.left is not None:
                    next_layer.append(node.left)
                if node.right is not None:
                    next_layer.append(node.right)

        return depth
