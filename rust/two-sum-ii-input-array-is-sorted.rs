impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        for (index1, num) in numbers.iter().enumerate() {
            let diff = target - num;
            for index2 in (index1 + 1)..numbers.len() {
                println!("comparing {} & {}", numbers[index2], diff);
                if numbers[index2] == diff {
                    return Vec::from([(index1 + 1) as i32, (index2 + 1) as i32]);
                }
            }
        }
        return Vec::from([0 as i32, 1 as i32]);
    }
}
