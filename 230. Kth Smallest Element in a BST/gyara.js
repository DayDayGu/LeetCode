/**
 * Definition for a binary tree node.
 * function TreeNode(val) {
 *     this.val = val;
 *     this.left = this.right = null;
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthSmallest = function(root, k) {
    let cnt = 0;
    let dfs = node => {
        if (node.left !== null) {
            let l = dfs(node.left);
            if (l !== undefined) {
                return l;
            }
        }
        if ( ++cnt === k ) {
            return node.val;
        }
        if (node.right !== null) {
            return dfs(node.right);
        }
    };
    return dfs(root);
};
