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
