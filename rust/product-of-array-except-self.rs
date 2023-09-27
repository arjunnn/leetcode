impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut output: Vec<i32> = vec![];
        let mut product = 1;
        for i in 0..nums.len() {
            output.push(1);
            output[i] = product;
            product *= nums[i];
        }
        product = 1;
        for i in (0..nums.len()).rev() {
            output[i] *= product;
            product *= nums[i];
        }
        return output;
    }
}
