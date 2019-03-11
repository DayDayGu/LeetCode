/*
 * @lc app=leetcode id=67 lang=rust
 *
 * [67] Add Binary
 *
 * https://leetcode.com/problems/add-binary/description/
 *
 * algorithms
 * Easy (38.02%)
 * Total Accepted:    279.2K
 * Total Submissions: 733.6K
 * Testcase Example:  '"11"\n"1"'
 *
 * Given two binary strings, return their sum (also a binary string).
 * 
 * The input strings are both non-empty and contains only characters 1 or 0.
 * 
 * Example 1:
 * 
 * 
 * Input: a = "11", b = "1"
 * Output: "100"
 * 
 * Example 2:
 * 
 * 
 * Input: a = "1010", b = "1011"
 * Output: "10101"
 * 
 */
struct Solution;

impl Solution {
    pub fn add_binary(a: String, b: String) -> String {
        const ZERO: u8 = 48;
        const ONE: u8 = 49;
        let ba = a.into_bytes();
        let bb = b.into_bytes();
        let mut res = Vec::new();
        let mut ca = ba.len();
        let mut cb = bb.len();
        let ll = std::cmp::max(ca, cb);
        let mut sa = ZERO;  // stack a
        // flag
        let mut fa = false;
        let mut fb = false;
        for _i in 0..ll {
            ca = if ca > 0 {
                ca - 1
            } else {
                fa = true;
                0
            };
            cb = if cb > 0 {
                cb - 1
            } else {
                fb = true;
                0
            };
            if fa {
                res.push(match sa {
                    ZERO => bb[cb],
                    _ => match bb[cb] {
                        ZERO => {
                            sa = ZERO;
                            ONE
                        },
                        _ => ZERO
                    }
                });
            } else if fb {
                res.push(match sa {
                    ZERO => ba[ca],
                    _ => match ba[ca] {
                        ZERO => {
                            sa = ZERO;
                            ONE
                        },
                        _ => ZERO
                    }
                })
            } else if ba[ca] == ONE && bb[cb] == ONE {
                res.push(sa);
                sa = ONE;
            } else if ba[ca] == ONE || bb[cb] == ONE {
                res.push(match sa {
                    ZERO => ONE,
                    _ => ZERO,
                })
            } else {
                res.push(sa);
                sa = ZERO;
            }
        }
        if sa == ONE {
            res.push(sa);
        }
        res.reverse();
        String::from_utf8(res).unwrap()
    }
}

fn main() {
    let a = String::from("1");
    let b = String::from("11");
    let res = Solution::add_binary(a, b);
    println!("{}", res);
}
