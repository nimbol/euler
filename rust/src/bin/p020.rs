use num_bigint::BigUint;
use num_traits::identities::One;

/// # Factorial digit sum
/// n! means n × (n − 1) × ... × 3 × 2 × 1
///
/// For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
/// and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
///
/// Find the sum of the digits in the number 100!
fn main() {
    println!("{}", solve(100));
}

fn solve(n: u8) -> u32 {
    factorial(n).to_radix_be(10).iter().map(|&d| d as u32).sum()
}

fn factorial(n: u8) -> BigUint {
    (2..=n).fold(BigUint::one(), |acc, n| acc * n)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn factorial_10() {
        assert_eq!(BigUint::from(3_628_800u64), factorial(10));
    }
    #[test]
    fn factorial_14() {
        assert_eq!(BigUint::from(87_178_291_200u64), factorial(14));
    }
    #[test]
    fn solve_10() {
        assert_eq!(27, solve(10));
    }
    #[test]
    fn solve_14() {
        assert_eq!(45, solve(14));
    }
}
