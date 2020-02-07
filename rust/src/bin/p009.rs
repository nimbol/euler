/// A Pythagorean triplet is a set of three natural numbers, `a < b < c`, for which,
/// ```
/// a² + b² = c²
/// ```
/// For example, 3² + 4² = 9 + 16 = 25 = 5².
///
/// There exists exactly one Pythagorean triplet for which `a + b + c = 1000`.
/// Find the product `abc`.
pub fn main() {
    println!("{}", solve(1000).unwrap());
}

fn solve(sum: u64) -> Option<u64> {
    for a in 1..sum / 2 {
        for b in a..sum {
            if let Some(c) = sum.checked_sub(a + b) {
                if a.pow(2) + b.pow(2) == c.pow(2) {
                    return Some(a * b * c);
                }
            } else {
                break;
            }
        }
    }
    None
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn solve_12() {
        assert_eq!(solve(12), Some(60));
    }

    #[test]
    fn solve_100() {
        assert_eq!(solve(100), None);
    }

    #[test]
    fn solve_1000() {
        assert_eq!(solve(1000), Some(31875000));
    }
}
