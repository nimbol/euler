fn main() {
    println!("{}", solve(4_000_000));
}

fn solve(limit: u32) -> u32 {
    Fibonacci::new().take_while(|x| x < &limit).step_by(3).sum()
}

struct Fibonacci {
    a: u32,
    b: u32,
}

impl Fibonacci {
    fn new() -> Fibonacci {
        Fibonacci { a: 0, b: 1 }
    }
}

impl Iterator for Fibonacci {
    type Item = u32;

    fn next(&mut self) -> Option<u32> {
        let result = self.a;
        self.a = self.b;
        self.b = self.b + result;
        
        Some(result)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn solution() {
        assert_eq!(solve(4_000_000), 4613732);
    }
}