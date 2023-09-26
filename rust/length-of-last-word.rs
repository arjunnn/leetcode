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

impl Solution {
    pub fn length_of_last_word(s: String) -> i32 {
        let mut i = 0;
        let mut start = false;
        for (index, c) in s.chars().rev().enumerate() {
            if c != ' ' {
                i += 1;
                start = true;
            } else if c == ' ' && start {
                return i;
            }
        }
        return i;
    }
}


