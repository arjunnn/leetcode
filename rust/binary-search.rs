impl Solution {
    pub fn search(nums: Vec<i32>, target: i32) -> i32 {
        if nums.contains(&target) {
            return nums.iter().position(|&r| r == target).unwrap() as i32;
        }
        return -1;
    }
}