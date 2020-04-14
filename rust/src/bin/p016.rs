use num_bigint::BigUint;
use num_traits::pow::Pow;

/// # Power digit sum
/// 2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
///
/// What is the sum of the digits of the number 2^1000?
fn main() {
    println!("{}", solve(BigUint::new(vec![2]).pow(1000u64)));
}
fn solve(n: BigUint) -> u32 {
    n.to_string().chars().filter_map(|c| c.to_digit(10)).sum()
}
