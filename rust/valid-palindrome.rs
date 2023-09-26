impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut an: Vec<char> = vec![];
        for c in s.chars() {
            let mut x = match c {
                'a'..='z' => Some(c),
                'A'..='Z' => Some(c.to_ascii_lowercase()),
                '0'..='9' => Some(c),
                _ => None,
            };
            if x.is_some() {
                an.push(x.unwrap());
            }
        }
        if an.len() <= 1 {
            return true;
        }
        let mut i = 0;
        let mut j = an.len() - 1;
        while j >= i {
            if an[i] != an[j] {
                return false;
            }
            i += 1;
            j -= 1;
        }

        return true;
    }
}
