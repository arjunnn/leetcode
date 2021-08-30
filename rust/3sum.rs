use std::collections::HashSet;
use std::iter::FromIterator;

impl Solution {
    pub fn three_sum(mut nums: Vec<i32>) -> Vec<Vec<i32>> {
        nums.sort_unstable();
        let mut result: HashSet<Vec<i32>> = HashSet::new();
        for i in 0..nums.len() {
            let mut l = i + 1;
            let mut r = nums.len() - 1;
            let mut target = 0 - nums[i];
            while l < r {
                if nums[l] + nums[r] == target {
                    result.insert(vec![nums[i], nums[l], nums[r]]);
                    l += 1;
                    r -= 1;
                
                } else if nums[l] + nums[r] < target {
                    l += 1;
                    
                } else {
                    r -= 1;
                }
            }
        }
        return Vec::from_iter(result);
    }
}