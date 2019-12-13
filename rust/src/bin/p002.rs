fn main() {
    println!("{}", solve(4_000_000));
}

fn solve(limit: u32) -> u32 {
    let mut seq = vec![0, 1];

    loop {
        let n = seq.iter().rev().take(2).sum();
        if n < limit {
            seq.push(n);
        } else {
            break;
        }
    }

    seq.iter().filter(|x| **x % 2 == 0).sum()
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn solution() {
        assert_eq!(solve(4_000_000), 4613732);
    }
}
