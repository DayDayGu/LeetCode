struct Solution;

impl Solution {
    pub fn move_zeroes(nums: &mut Vec<i32>) {
        let len = nums.len();
        let mut offset = 0;
        for i in 0..len {
            while i+offset < len && nums[i + offset] == 0 {
                offset += 1;
            }
            if offset != 0 && i + offset < len {
                nums[i] = nums[i + offset];
            } else if offset != 0 {
                for j in i..len {
                    nums[j] = 0;
                }
                break;
            }
        }
    }
}

fn main() {
    let mut input = vec![0i32, 1, 0];
    Solution::move_zeroes(&mut input);
    println!("{:?}", input);
    input = vec![1];
    Solution::move_zeroes(&mut input);
    println!("{:?}", input);
}