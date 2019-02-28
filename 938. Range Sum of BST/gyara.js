/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} L
 * @param {number} R
 * @return {number}
 */
var rangeSumBST = function(root, L, R) {
    let re = 0;
    if (root === null) {
      return 0;
    }
    if (root.val < R) {
      re += rangeSumBST(root.right, L, R);
    }
    if (root.val > L) {
      re += rangeSumBST(root.left, L, R);
    }
    if (root.val >= L && root.val <= R) {
      re += root.val;
    }
    return re;
};