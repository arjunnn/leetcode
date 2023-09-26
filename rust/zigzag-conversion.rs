impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if num_rows == 1 || num_rows > s.len() as i32 {
            return s;
        }
        let mut output = vec![];
        for i in 1..=num_rows {
            output.push("".to_string());
        }
        let mut index: i32 = 0;
        let mut step = 1;
        for letter in s.chars() {
            output[index as usize] += &letter.to_string();
            if index == 0 {
                step = 1;
            } else if index == num_rows - 1 {
                step = -1;
            }
            index += step;
        }
        return output.join("");
    }
}
