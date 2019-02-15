struct Solution{}

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut r = height.len();
        let mut l = r;
        for i in 0..r {
            if height[i] > 0 {
                l = i;
                break;
            }
        }
        if l == r {  // all 0
            return 0;
        }
        for i in (0..r).rev() {
            if height[i] > 0 {
                r = i;
                break;
            }
        }
        if (r - l) < 2 {   // need at least 3 block
            return 0;
        } 
        let mut res = 0;
        'out: loop {
            // println!("{} {} {}", l, r, res);
            let mut level = height[l];
            for i in l+1..=r {
                if height[i] >= height[l] {
                    for j in l+1..i {
                        res += level - height[j];
                    }
                    l = i;
                    continue 'out;
                }
            }
            // if l is max
            level = height[r];
            for i in (l+1..r).rev() {
                if height[i] < level {
                    res += level - height[i];
                }
                if height[i] > level {
                    r = i;
                    continue 'out;
                }
            }
            break;
        }
        res
    }
}

fn main() {
    println!("{:?}", Solution::trap(vec![2,0,2]));
    println!("{:?}", Solution::trap(vec![2,0,3,0,4,2,3]));
    println!("{:?}", Solution::trap(vec![0,1,0,2,1,0,1,3,2,1,2,1]));
}