use std::ops::Range;

/// # Number letter counts
/// If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are
/// 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
///
/// If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
/// how many letters would be used?
///
///
/// *NOTE:* Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains
/// 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing
/// out numbers is in compliance with British usage.
fn main() {
    println!("{}", solve(1..1001));
}

fn solve(range: Range<u32>) -> usize {
    range
        .map(|n| int_to_word(n))
        .collect::<Vec<_>>()
        .join("")
        .len()
}

/// Write out an integer into words, omitting hyphens and spaces.
fn int_to_word(n: u32) -> String {
    let mut r = String::new();

    // Special cases 10..=19 for last two digits.
    r += match n % 100 {
        10 => "ten",
        11 => "eleven",
        12 => "twelve",
        13 => "thirteen",
        14 => "fourteen",
        15 => "fifteen",
        16 => "sixteen",
        17 => "seventeen",
        18 => "eighteen",
        19 => "nineteen",
        _ => "",
    };
    // All other cases for last two digits.
    if r == "" {
        r += match (n % 100) / 10 {
            2 => "twenty",
            3 => "thirty",
            4 => "forty",
            5 => "fifty",
            6 => "sixty",
            7 => "seventy",
            8 => "eighty",
            9 => "ninety",
            _ => "",
        };
        r += match n % 10 {
            1 => "one",
            2 => "two",
            3 => "three",
            4 => "four",
            5 => "five",
            6 => "six",
            7 => "seven",
            8 => "eight",
            9 => "nine",
            _ => "",
        };
    }

    // Hundreds digit.
    let dh = (n / 100) % 10;
    if dh > 0 {
        let h = int_to_word(dh) + "hundred";
        if r == "" {
            r = h;
        } else {
            r = h + "and" + &r;
        }
    }

    // Thousands up to a million.
    let dt = (n / 1000) % 1000;
    if dt > 0 {
        let t = int_to_word(dt) + "thousand";
        if r == "" {
            r = t;
        } else {
            r = t + "and" + &r;
        }
    }

    r
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn solve_1_5() {
        assert_eq!(19, solve(1..6));
    }
    #[test]
    fn int_to_word_9() {
        assert_eq!("nine", int_to_word(9));
    }
    #[test]
    fn int_to_word_19() {
        assert_eq!("nineteen", int_to_word(19));
    }
    #[test]
    fn int_to_word_90() {
        assert_eq!("ninety", int_to_word(90));
    }
    #[test]
    fn int_to_word_99() {
        assert_eq!("ninetynine", int_to_word(99));
    }
    #[test]
    fn int_to_word_100() {
        assert_eq!("onehundred", int_to_word(100));
    }
    #[test]
    fn int_to_word_999() {
        assert_eq!("ninehundredandninetynine", int_to_word(999));
    }
    #[test]
    fn int_to_word_1000() {
        assert_eq!("onethousand", int_to_word(1000));
    }
}
