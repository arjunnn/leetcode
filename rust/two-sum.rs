use std::collections::HashSet;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        for i in 0..nums.len() {
            let diff = target - nums[i];
            if nums.contains(&diff) {
                let diff_index = nums.iter().position(|&x| x == diff).unwrap();
                if i != diff_index {
                    return Vec::from([i as i32, diff_index as i32])
                }
            } 
        }
        Vec::new()
    }
}