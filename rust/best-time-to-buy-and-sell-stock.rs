use std::cmp::{max, min};

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max_profit = 0;
        let mut min_price = prices[0];
        for i in 0..prices.len() {
            max_profit = max(max_profit, prices[i] - min_price);
            min_price = min(min_price, prices[i])
        }
        return max_profit;
    }
}

use std::cmp::max;

impl Solution {
    pub fn max_profit(prices: Vec<i32>) -> i32 {
        let mut max_profit: i32 = 0;
        let mut min_buy: i32 = prices[0];
        for i in 1..prices.len() {
            if prices[i] < min_buy {
                min_buy = prices[i]
            } else {
                max_profit = max(max_profit, prices[i] - min_buy)
            }
        }
        max_profit
    }
}