use std::collections::HashMap;
use std::iter;

/// Break an integer down into its prime factors, represented as <base, exponent>.
pub fn factors(n: u64) -> HashMap<u64, u32> {
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

/// Compute primes one by one using a naive (i.e. slow) algorithm.
pub fn iterator() -> impl Iterator<Item = u64> {
    iter::once(2).chain(PrimeIterator::new())
}

/// Iterator that computes primes one by one using a naive (i.e. slow) algorithm.
/// Sequence starts from 3. For the full sequence including 2 use the `iterator()` function.
struct PrimeIterator {
    primes: Vec<u64>,
}

impl PrimeIterator {
    fn new() -> PrimeIterator {
        PrimeIterator { primes: vec![] }
    }
}

impl Iterator for PrimeIterator {
    type Item = u64;

    fn next(&mut self) -> Option<Self::Item> {
        let last = *self.primes.last().unwrap_or(&1);

        let p = (last + 2..)
            .step_by(2)
            .filter(|&n| {
                let sqrt = (n as f64).sqrt();
                self.primes
                    .iter()
                    .take_while(|&p| (*p as f64) <= sqrt)
                    .all(|&p| n % p > 0)
            })
            .next()
            .unwrap();

        self.primes.push(p);
        Some(p)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn iterator_take_15() {
        assert_eq!(
            iterator().take(15).collect::<Vec<_>>(),
            vec![2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
        );
    }
    #[test]
    fn factors_13195() {
        let expected: HashMap<_, _> = [(5, 1), (7, 1), (13, 1), (29, 1)].iter().cloned().collect();

        assert_eq!(factors(13195), expected);
    }

    #[test]
    fn factors_600851475143() {
        let expected: HashMap<_, _> = [(71, 1), (839, 1), (1471, 1), (6857, 1)]
            .iter()
            .cloned()
            .collect();

        assert_eq!(factors(600851475143), expected);
    }

    #[test]
    fn factors_0() {
        assert_eq!(factors(0), HashMap::new());
    }

    #[test]
    fn factors_1() {
        assert_eq!(factors(1), HashMap::new());
    }

    #[test]
    fn factors_2() {
        assert_eq!(
            factors(2),
            [(2, 1)].iter().cloned().collect::<HashMap<_, _>>()
        );
    }

    #[test]
    fn factors_64() {
        assert_eq!(
            factors(64),
            [(2, 6)].iter().cloned().collect::<HashMap<_, _>>()
        );
    }

    #[test]
    fn factors_3() {
        assert_eq!(
            factors(3),
            [(3, 1)].iter().cloned().collect::<HashMap<_, _>>()
        );
    }
}
