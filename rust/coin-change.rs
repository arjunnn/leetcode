use std::cmp::{min};

impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let max_value = amount + 1;
        let mut amounts = vec![max_value; max_value as usize];
        amounts[0] = 0;
        for i in 1..=amount {
            for coin in &coins {
                if i - coin >= 0 {
                    amounts[i as usize] = min(amounts[i as usize], 1 + amounts[(i - coin) as usize]);
                }
            }
        }
        if amounts[amount as usize] == max_value {
            -1
        } else {
            amounts[amount as usize]
        }
    }
}