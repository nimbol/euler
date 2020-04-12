/// # Longest Collatz sequence
/// The following iterative sequence is defined for the set of positive integers:
///
/// n → n/2 (n is even)
/// n → 3n + 1 (n is odd)
///
/// Using the rule above and starting with 13, we generate the following sequence:
///
/// 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
/// It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
/// Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers
/// finish at 1.
///
/// Which starting number, under one million, produces the longest chain?
///
/// NOTE: Once the chain starts the terms are allowed to go above one million.
fn main() {
    println!("{:?}", solve(1_000_000));
}

fn solve(stop: u64) -> (u64, usize) {
    let mut result = 0;
    let mut longest = 0;
    let start = stop / 2;
    for n in start..stop {
        let seq = collatz_seq(n);
        if seq.len() > longest {
            longest = seq.len();
            result = n;
            // println!("len: {}, n: {}", longest, n);
        }
    }
    (result, longest)
}

fn collatz_seq(n: u64) -> Vec<u64> {
    let mut result = vec![n];
    let mut n = n;
    loop {
        if n == 1 {
            break result;
        }
        if n % 2 == 0 {
            n /= 2;
        } else {
            n = 3 * n + 1;
        }
        result.push(n);
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn collatz_seq_13() {
        assert_eq!(vec![13, 40, 20, 10, 5, 16, 8, 4, 2, 1], collatz_seq(13));
    }
}
