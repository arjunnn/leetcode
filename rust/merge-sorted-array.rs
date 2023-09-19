impl Solution {
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, n: i32) {
        for i in 0..n {
            nums1.pop();
        }
        nums1.extend(nums2.iter());
        nums1.sort();
    }
}
