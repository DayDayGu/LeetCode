// Definition for a binary tree node.
// #[derive(Debug, PartialEq, Eq)]
// pub struct TreeNode {
//   pub val: i32,
//   pub left: Option<Rc<RefCell<TreeNode>>>,
//   pub right: Option<Rc<RefCell<TreeNode>>>,
// }
// 
// impl TreeNode {
//   #[inline]
//   pub fn new(val: i32) -> Self {
//     TreeNode {
//       val,
//       left: None,
//       right: None
//     }
//   }
// }
use std::rc::Rc;
use std::cell::RefCell;
impl Solution {
    pub fn dfs(root: &Option<Rc<RefCell<TreeNode>>>, depth: i32) -> i32 {
        if let Some(node) = root {
            let l = Solution::dfs(&node.borrow().left, depth);
            let r = Solution::dfs(&node.borrow().right, depth);
            return std::cmp::max(l, r) + 1;
        } else {
            return depth;
        }
    }

    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut res: i32 = 0;
        return Solution::dfs(&root, 0);
    }
}