use std::cmp;

impl Solution {
    pub fn max_area(height: Vec<i32>) -> i32 {
        let mut i = 0;
        let mut j = height.len() - 1;
        let mut area = 0;
        while i < j {
            area = cmp::max(area, (j - i) * cmp::min(height[i], height[j]) as usize);
            if height[i] > height[j] {
                j -= 1;
            } else {
                i += 1;
            }
        }
        return area as i32
    }
}