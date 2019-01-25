struct Solution;

impl Solution {

    pub fn permute(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort_unstable();
        let mut res = vec![nums.clone()];
        let mut dir = vec![0; nums.len()];
        'out: loop {
            let mut max_ele = 0;
            let mut max_tar = 0;
            let mut active = false;
            for i in 0..nums.len() {
                let target = match dir[i] {
                   0 =>  match i {
                       0 => nums.len(),
                       _ => i - 1,
                   },
                   _ => i + 1,
                };
                if target < nums.len() && nums[i] > nums[target] {
                    if !active || (active && nums[i] > nums[max_ele]) {
                        active = true;
                        max_ele = i;
                        max_tar = target;
                    };
                };
            }
            if !active {
                break 'out;
            }
            let st = nums[max_ele];
            nums.swap(max_ele, max_tar);
            dir.swap(max_ele, max_tar);
            for i in 0..nums.len() {
                if nums[i] > st {
                    dir[i] = match dir[i] {
                        0 => 1,
                        _ => 0,
                    }
                }
            }
            res.push(nums.clone());
        }
        res
    }
}

fn main() {
    let test = vec![1, 2, 3];
    println!("{:?}", Solution::permute(test));
}