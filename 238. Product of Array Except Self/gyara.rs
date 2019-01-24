struct Solution;

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut r = 1;
        let mut res = nums.clone();
        for i in 1..res.len() {
            res[i] *= res[i-1];
        }
        for i in (0..res.len()).rev() {
            if i > 0 {
                res[i] = res[i-1] * r;
                r *= nums[i];
            } else {
                res[i] = r;
            }
        }
        res
    }
}

fn main() {
    let nums = vec![1, 2, 3, 4];
    println!("{:?}", Solution::product_except_self(nums));
}
