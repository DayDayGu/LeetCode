# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        layer = [ root ]
        next_layer = []
        i = 0
        while ( len(layer)>0 ):
            for node in layer:
                if node.left is not None:
                    next_layer.append(node.left)
                if node.right is not None:
                    next_layer.append(node.right)
            layer = next_layer
            next_layer = []
            i+=1 
        return i