use std::fs;

fn main() {
    let filename = "/home/frans/repo/euler/rust/asset/p022_names.txt";
    println!("{}", solve(filename.to_owned()));
}

fn solve(filename: String) -> u64 {
    let s = fs::read_to_string(filename).unwrap();
    let mut v: Vec<&str> = s.split(|c: char| c == ',').collect();
    v.sort();

    // Letters are scored based on alphabetic position. Score double quotes at zero points.
    let letters = "\"ABCDEFGHIJKLMNOPQRSTUVWXYZ";

    v.iter()
        .map(|&name| {
            name.chars()
                .map(|c| letters.find(c).unwrap() as u64)
                .sum::<u64>()
        })
        .enumerate()
        .fold(0, |acc, (i, n)| acc + n * (i as u64 + 1))
}
