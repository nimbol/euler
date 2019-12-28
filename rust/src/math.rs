use std::collections::HashMap;

pub fn prime_factors(n: u64) -> HashMap<u64, u64> {
    let mut result = HashMap::new();
    let mut n = n;

    for d in (2..3).chain((3..=n).step_by(2)) {
        if n <= 1 {
            break;
        }
        while n % d == 0 {
            *result.entry(d).or_insert(0) += 1;
            n /= d;
        }
    }

    result
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn prime_factors_13195() {
        let factors = [(5, 1), (7, 1), (13, 1), (29, 1)];
        let expected: HashMap<_, _> = factors.iter().cloned().collect();

        assert_eq!(prime_factors(13195), expected);
    }

    #[test]
    fn prime_factors_600851475143() {
        let factors = [(71, 1), (839, 1), (1471, 1), (6857, 1)];
        let expected: HashMap<_, _> = factors.iter().cloned().collect();

        assert_eq!(prime_factors(600851475143), expected);
    }

    #[test]
    fn prime_factors_0() {
        assert_eq!(prime_factors(0), HashMap::new());
    }

    #[test]
    fn prime_factors_1() {
        assert_eq!(prime_factors(1), HashMap::new());
    }

    #[test]
    fn prime_factors_2() {
        assert_eq!(prime_factors(2), [(2, 1)].iter().cloned().collect::<HashMap<_, _>>());
    }

    #[test]
    fn prime_factors_64() {
        assert_eq!(prime_factors(64), [(2, 6)].iter().cloned().collect::<HashMap<_, _>>());
    }

    #[test]
    fn prime_factors_3() {
        assert_eq!(prime_factors(3), [(3, 1)].iter().cloned().collect::<HashMap<_, _>>());
    }
}
