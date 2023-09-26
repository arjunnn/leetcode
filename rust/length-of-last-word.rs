impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        return s
            .split(" ")
            .into_iter()
            .filter(|w| !w.is_empty())
            .last()
            .unwrap()
            .len() as i32;
    }
}
