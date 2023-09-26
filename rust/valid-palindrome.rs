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

impl Solution {
    fn is_alpha_numeric(c: char) -> bool {
        return match c {
            'a'..='z' => true,
            'A'..='Z' => true,
            '0'..='9' => true,
            _ => false,
        };
    }

    pub fn is_palindrome(s: String) -> bool {
        let an: Vec<char> = s.chars().collect();
        let mut i = 0;
        let mut j = an.len() - 1;
        while j > i {
            if !Solution::is_alpha_numeric(an[i]) {
                i += 1;
                continue;
            }
            if !Solution::is_alpha_numeric(an[j]) {
                j -= 1;
                continue;
            }
            if an[i].to_ascii_lowercase() != an[j].to_ascii_lowercase() {
                return false;
            }
            i += 1;
            j -= 1;
        }
        return true;
    }
}
