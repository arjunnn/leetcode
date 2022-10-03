impl Solution {
    pub fn pivot_index(nums: Vec<i32>) -> i32 {
        let mut left_sum = 0;
        let mut right_sum: i32 = nums.iter().sum();
        for index in 0..nums.len() {
            right_sum -= nums[index];
            if left_sum == right_sum {
                return index as i32;
            }
            left_sum += nums[index];
        }
        return -1 as i32;
    }
}