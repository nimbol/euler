use euler::prime;

/// # Summation of primes
/// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
///
/// Find the sum of all the primes below two million.
fn main() {
    println!("{}", solve(2_000_000));
}

pub fn solve(limit: u64) -> u64 {
    prime::iterator().take_while(|&p| p < limit).sum()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn solve_10() {
        assert_eq!(solve(10), 17);
    }

    #[test]
    fn solve_2m() {
        assert_eq!(solve(2_000_000), 142_913_828_922);
    }
}
