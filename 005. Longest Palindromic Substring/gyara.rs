/*
 * @lc app=leetcode id=5 lang=rust
 *
 * [5] Longest Palindromic Substring
 *
 * https://leetcode.com/problems/longest-palindromic-substring/description/
 *
 * algorithms
 * Medium (26.66%)
 * Total Accepted:    496.7K
 * Total Submissions: 1.9M
 * Testcase Example:  '"babad"'
 *
 * Given a string s, find the longest palindromic substring in s. You may
 * assume that the maximum length of s is 1000.
 * 
 * Example 1:
 * 
 * 
 * Input: "babad"
 * Output: "bab"
 * Note: "aba" is also a valid answer.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: "cbbd"
 * Output: "bb"
 * 
 * 
 */
struct Solution;

impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        if s.len() == 0 {
            return String::from("");
        }
        let mut max_len = 0;
        let mut max_start = 0;
        let s_str = s.into_bytes();
        for i in 1..s_str.len() {  // aba
            let mut i_len = 0;
            for len in 1..=i {
                let l = i - len;
                let r = i + len;
                if r >= s_str.len() || s_str[l] != s_str[r] {
                    break;
                } else {
                    i_len = len;
                }
            }
            if i_len * 2 > max_len {
                max_len = i_len * 2;
                max_start = i - i_len;
            }
        }
        for i in 0..(s_str.len() - 1) {  // abba
            let mut ii_len = 0;
            for len in 0..=i {
                let l = i - len;
                let r = i + len + 1;
                if r >= s_str.len() || s_str[l] != s_str[r] {
                    break;
                } else {
                    ii_len = len;
                }
            }
            if s_str[i] == s_str[i+1] && ii_len * 2 + 1 > max_len {
                max_len = ii_len * 2 + 1;
                max_start = i - ii_len;
            }
        }
        let l = max_start;
        let r = max_start + max_len;
        unsafe {
            String::from_utf8_unchecked(s_str).get_unchecked(l..=r).to_string()
        }

    }
}

fn main() {
    let s = String::from("cbbd");
    println!("{}" ,Solution::longest_palindrome(s));
}

