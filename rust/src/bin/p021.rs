use std::collections::HashMap;

/// # Amicable numbers
/// Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly
/// into n).
/// If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are
/// called amicable numbers.
///
/// For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
/// therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
///
/// Evaluate the sum of all the amicable numbers under 10000.
fn main() {
    println!("{}", solve(10_000));
}

fn solve(limit: u64) -> u64 {
    let mut sum = 0;
    let mut cache: HashMap<u64, u64> = HashMap::new();

    for n in 2..limit {
        let a: u64 = *cache.entry(n).or_insert_with(|| sum_proper_divisors(n));
        if a == 1 || a >= limit {
            continue;
        }

        let b: u64 = *cache.entry(a).or_insert_with(|| sum_proper_divisors(a));
        if b == n && a != b {
            sum += a;
        }
    }

    sum
}

fn sum_proper_divisors(n: u64) -> u64 {
    proper_divisors(n).iter().sum()
}

fn proper_divisors(n: u64) -> Vec<u64> {
    let mut divs = vec![1];
    let sqrt = (n as f64).sqrt() as u64;
    for d in 2..=sqrt {
        if n % d == 0 {
            divs.push(d);

            let q = n / d;
            if q != d {
                divs.push(q);
            }
        }
    }
    divs
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn solve_250() {
        assert_eq!(0, solve(250));
    }
    #[test]
    fn solve_285() {
        assert_eq!(504, solve(285));
    }
    #[test]
    fn proper_divisors_16() {
        assert_eq!(vec![1, 2, 8, 4], proper_divisors(16));
    }
    #[test]
    fn proper_divisors_220() {
        assert_eq!(
            vec![1, 2, 110, 4, 55, 5, 44, 10, 22, 11, 20],
            proper_divisors(220)
        );
    }
    #[test]
    fn proper_divisors_284() {
        assert_eq!(vec![1, 2, 142, 4, 71], proper_divisors(284));
    }
    #[test]
    fn sum_proper_divisors_220() {
        assert_eq!(284, sum_proper_divisors(220));
    }
    #[test]
    fn sum_proper_divisors_284() {
        assert_eq!(220, sum_proper_divisors(284));
    }
}
