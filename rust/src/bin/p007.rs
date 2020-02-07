use euler::prime;

/// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
///
/// What is the 10 001st prime number?
fn main() {
    println!("{}", solve(10001));
}

fn solve(n: usize) -> u64 {
    prime::iterator().take(n).last().unwrap()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn solve_6() {
        assert_eq!(13, solve(6));
    }

    #[test]
    fn solve_10001() {
        assert_eq!(104743, solve(10001));
    }
}
