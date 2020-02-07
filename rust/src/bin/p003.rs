use euler::prime;

/// # Largest prime factor
/// The prime factors of 13195 are 5, 7, 13 and 29.
///
/// What is the largest prime factor of the number 600851475143 ?
fn main() {
    println!("{}", solve(600_851_475_143));
}

fn solve(n: u64) -> u64 {
    match prime::factors(n).keys().max() {
        Some(&p) => p,
        None => 0,
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn solve_13195() {
        assert_eq!(solve(13195), 29);
    }

    #[test]
    fn solve_600851475143() {
        assert_eq!(solve(600851475143), 6857);
    }

    #[test]
    fn solve_0() {
        assert_eq!(solve(0), 0);
    }

    #[test]
    fn solve_1() {
        assert_eq!(solve(1), 0);
    }
}
