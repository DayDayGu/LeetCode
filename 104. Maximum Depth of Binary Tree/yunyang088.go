/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	return max(1+maxDepth(root.Left), 1+maxDepth(root.Right))
}

func max(x, y int) int {
	if x < y {
		return y
	}
	return x
}
