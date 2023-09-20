impl Solution {
    pub fn majority_element(nums: Vec<i32>) -> i32 {
        let mut num = nums[0];
        let mut count = 1;
        for i in 0..nums.len() {
            if nums[i] != num {
                count -= 1;
                if count == 0 {
                    num = nums[i];
                    count = 1;
                }
            } else {
                count += 1;
            }
        }
        return num;
    }
}