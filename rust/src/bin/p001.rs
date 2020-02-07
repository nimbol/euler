/// # Multiples of 3 and 5
/// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
/// The sum of these multiples is 23.
///
/// Find the sum of all the multiples of 3 or 5 below 1000.
fn main() {
    println!("{}", solve(1000));
}

fn solve(n: u32) -> u32 {
    (1..n).filter(|x| x % 3 == 0 || x % 5 == 0).sum()
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn solution() {
        assert_eq!(solve(1000), 233168);
    }
}
