#![feature(nll)]
struct Solution;

impl Solution {
    pub fn four_sum_count(a: Vec<i32>, b: Vec<i32>, c: Vec<i32>, d: Vec<i32>) -> i32 {
        let mut tree = std::collections::BTreeMap::new();
        let len = a.len();
        // build tree
        for i in 0..len {
            for j in 0..len {
                let add = a[i] + b[j];
                match tree.get_mut(&add) {
                    Some(val) => {;
                        *val = *val + 1;
                    },
                    None => {
                        tree.insert(add, 1);
                    }
                }
            }
        }
        // resolve
        let mut res = 0;
        for i in 0..len {
            for j in 0..len {
                let add = -1 * ( c[i] + d[j] );
                match tree.get(&add) {
                    Some(val) => {
                        res += *val;
                    },
                    None => {}
                }
            }
        }
        res
    }
}

fn main() {
    let a = vec![ 1, 2];
    let b = vec![-2,-1];
    let c = vec![-1, 2];
    let d = vec![ 0, 2];
    let out = Solution::four_sum_count(a, b, c, d);
    println!("{}", out);
}