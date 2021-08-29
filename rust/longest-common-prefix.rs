pub fn main() -> () {
    dbg!("hello world");
    let strings: Vec<String> = vec![
            "flower".to_string(), "flair".to_string(), "flip".to_string(), "flower".to_string()
        ];
    dbg!(longest_common_prefix(strings));
}

fn longest_common_prefix(mut strings: Vec<String>) -> String {
    strings.sort_unstable();
    strings.dedup();
    let mut smallest = strings[0].len();
    for word in &strings {
        let len = word.len();
        smallest = if len < smallest {
            len
        } else { smallest };
    }
    strings = strings.into_iter().map(|x| x[..smallest].to_string()).collect();
    if strings.len() == 1 {
        return strings[0].to_string();
    }
    let mut prefix: String = "".to_string();
    let mut length = if prefix.len() > 0 {
        prefix.len()
    } else {
        1
    };
    loop {
        let mut truncated_strings: Vec<String> = strings
                                                    .clone()
                                                    .into_iter()
                                                    .map(|x| x[..length].to_string())
                                                    .collect();
        truncated_strings.dedup();
        if truncated_strings.len() == 1 {
            let first_word = truncated_strings[0];
            *prefix = first_word[..length];
            if prefix.len() == first_word.len() {
                return first_word.to_string();
            }
            if prefix.len() > first_word.len() {
                length += 1;
                continue;
            }
        }
        break;
    }
    // dbg!(prefix);
    dbg!("".to_string());
    // return "".to_string();
    return prefix.to_string();
}