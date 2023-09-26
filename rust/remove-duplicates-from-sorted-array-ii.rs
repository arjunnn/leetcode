impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut i = 0;
        let mut current = nums[i];
        let mut occurances = 0;
        while i < nums.len() {
            if nums[i] == current {
                occurances += 1;
                if occurances > 2 {
                    nums.remove(i);
                    i -= 1;
                }
            } else {
                current = nums[i];
                occurances = 1;
            }
            i += 1;
        }
        return nums.len() as i32;
    }
}

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        let mut i = 0;
        if nums.len() == 1 {
            return 1;
        }
        while i < nums.len() - 2 {
            if nums[i] == nums[i + 1] && nums[i + 1] == nums[i + 2] {
                let _ = nums.remove(i);
            } else {
                i += 1;
            }
        }
        return nums.len() as i32;
    }
}
