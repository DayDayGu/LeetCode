struct Solution;

impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut r = 1;
        let mut res = nums.clone();
        for i in 1..res.len() {
            res[i] *= res[i-1];
        }
        for i in 0..res.len() {
            let j = res.len() - i - 1;
            if j > 0 {
                res[j] = res[j-1] * r;
                r *= nums[j];
            } else {
                res[j] = r;
            }
        }
        res
    }
}

fn main() {
    let nums = vec![1, 2, 3, 4];
    println!("{:?}", Solution::product_except_self(nums));
}
