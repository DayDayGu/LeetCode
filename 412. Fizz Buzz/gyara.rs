struct Solution {}

impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {
        let mut res = Vec::with_capacity(n as usize);
        for i in 1..n+1 {
            let s = match i % 15 {
                0 => String::from("FizzBuzz"),
                3 | 6 | 9 | 12 => String::from("Fizz"),
                5 | 10 => String::from("Buzz"),
                _ => i.to_string(),
            };
            res.push(s);
        }
        res
    }
}

fn main() {
    let result = Solution::fizz_buzz(31);
    for i in result {
        println!("{}", i);
    }
}
