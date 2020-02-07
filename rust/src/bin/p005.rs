use euler::prime;
use std::collections::HashMap;

fn main() {
    println!("{}", solve(1..20));
}

fn solve<T: Iterator<Item = u64>>(seq: T) -> u64 {
    let mut max_factors: HashMap<u64, u32> = HashMap::new();
    let mut factors: Vec<_> = seq.flat_map(|n| prime::factors(n).into_iter()).collect();

    factors.sort();
    max_factors.extend(factors);

    max_factors.into_iter().map(|(a, b)| a.pow(b)).product()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn solve_1_10() {
        assert_eq!(solve(1..11), 2520);
    }

    #[test]
    fn solve_1_20() {
        assert_eq!(solve(1..21), 232792560);
    }
}
