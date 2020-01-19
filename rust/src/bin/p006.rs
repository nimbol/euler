use std::ops::Range;

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
