use std::ops::Range;

/// # Sum square difference
/// The sum of the squares of the first ten natural numbers is,
///
/// `1² + 2² + ... + 10² = 385`
///
/// The square of the sum of the first ten natural numbers is,
///
/// `(1 + 2 + ... + 10)² = 55² = 3025`
///
/// Hence the difference between the sum of the squares of the first ten natural numbers and the
/// square of the sum is `3025 − 385 = 2640`.
///
/// Find the difference between the sum of the squares of the first one hundred natural numbers and
/// the square of the sum.
fn main() {
    println!("{}", solve(1..101));
}

fn solve(range: Range<u64>) -> u64 {
    let sqsum = range.clone().sum::<u64>().pow(2);
    let sumsq = range.map(|x: u64| x.pow(2)).sum::<u64>();

    sqsum - sumsq
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_solve_10() {
        assert_eq!(solve(1..11), 2640);
    }

    #[test]
    fn test_solve_100() {
        assert_eq!(solve(1..101), 25164150);
    }
}
