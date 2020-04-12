use num_bigint::BigUint;

/// # Lattice paths
/// Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down,
/// there are exactly 6 routes to the bottom right corner.
///
/// How many such routes are there through a 20×20 grid?
fn main() {
    println!("{}", solve(20));
}

fn solve(grid_dim: u64) -> BigUint {
    pascals_triangle(2 * grid_dim, grid_dim)
}

fn pascals_triangle(n: u64, k: u64) -> BigUint {
    factorial(n) / (factorial(k) * factorial(n - k))
}

fn factorial(n: u64) -> BigUint {
    (2..=n).product()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn factorial_5() {
        assert_eq!(BigUint::from(120u64), factorial(5));
    }
    #[test]
    fn factorial_9() {
        assert_eq!(BigUint::from(362880u64), factorial(9));
    }
    #[test]
    fn pascals_triangle_0_0() {
        assert_eq!(BigUint::from(1u64), pascals_triangle(0, 0));
    }
    #[test]
    fn pascals_triangle_2_1() {
        assert_eq!(BigUint::from(2u64), pascals_triangle(2, 1));
    }
    #[test]
    fn pascals_triangle_4_2() {
        assert_eq!(BigUint::from(6u64), pascals_triangle(4, 2));
    }
    #[test]
    fn pascals_triangle_6_3() {
        assert_eq!(BigUint::from(20u64), pascals_triangle(6, 3));
    }
    #[test]
    fn solve_1() {
        assert_eq!(BigUint::from(2u64), solve(1));
    }
    #[test]
    fn solve_2() {
        assert_eq!(BigUint::from(6u64), solve(2));
    }
    #[test]
    fn solve_3() {
        assert_eq!(BigUint::from(20u64), solve(3));
    }
}
