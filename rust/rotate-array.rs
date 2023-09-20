impl Solution {
    pub fn rotate(nums: &mut Vec<i32>, mut k: i32) {
        k = k % nums.len() as i32;
        while k != 0 {
            let last = nums.pop().unwrap();
            nums.insert(0, last);
            k -= 1;
        }
    }
}
