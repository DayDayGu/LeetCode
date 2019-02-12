// Definition for singly-linked list.
// #[derive(PartialEq, Eq, Debug)]
// pub struct ListNode {
//   pub val: i32,
//   pub next: Option<Box<ListNode>>
// }
// 
// impl ListNode {
//   #[inline]
//   fn new(val: i32) -> Self {
//     ListNode {
//       next: None,
//       val
//     }
//   }
// }
impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut cur = head;
        let mut res = None;
        'out: loop {
            match cur {
                Some(node) => {
                    let mut nn = Box::new(ListNode::new(node.val));
                    nn.next = res;
                    res = Some(nn);
                    cur = node.next;
                },
                None => {
                    break 'out;
                }
            }
        }
        res
    }
}