fn main() {
    println!("{}", solve());
}

fn solve() -> u64 {
    let mut palindromes = vec![];
    for n1 in (901..=999).step_by(2) {
        let r = match n1 % 10 {
            9 => (901..=n1-8),
            7 => (907..=n1),
            3 => (903..=n1),
            _ => (0..=0),
        };
        for n2 in r.rev().step_by(10) {
            let p = n1 * n2;
            // Make palindromes "9nnnn9".
            if p < 900_000 {
                break;
            }
            if is_palindrome(p) {
                palindromes.push(p);
            }
        }
    }
    palindromes.sort();
    palindromes.pop().unwrap()
}

fn is_palindrome(n: u64) -> bool {
    let as_str = n.to_string();
    as_str == as_str.chars().rev().collect::<String>()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn solve_ok() {
        assert_eq!(solve(), 906609);
    }

    #[test]
    fn is_palindrome_true() {
        assert!(is_palindrome(12345678987654321));
    }

    #[test]
    fn is_palindrom_false() {
        assert!(!is_palindrome(123456789876543210));
    }
}
