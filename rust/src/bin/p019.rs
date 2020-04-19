/// # Counting Sundays
/// You are given the following information, but you may prefer to do some research for yourself.
///
/// * 1 Jan 1900 was a Monday.
/// * Thirty days has September,
///   April, June and November.
///   All the rest have thirty-one,
///   Saving February alone,
///   Which has twenty-eight, rain or shine.
///   And on leap years, twenty-nine.
/// * A leap year occurs on any year evenly divisible by 4, but not on a century unless it is
///   divisible by 400.
///
/// How many Sundays fell on the first of the month during the twentieth century
/// (1 Jan 1901 to 31 Dec 2000)?
fn main() {
    // Using `chrono` would be cheating. ;-)
    println!("{}", solve(1901, 2000));
}

fn solve(start: u16, stop: u16) -> u16 {
    let mut day_of_week: u16 = 0; // Monday
    let mut sundays = 0;

    // Fast forward from 1900 to starting year.
    for y in 1900..start {
        day_of_week += 365 + leap_day(y);
    }

    for y in start..=stop {
        for days in &[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] {
            day_of_week %= 7;

            // Check for Sunday.
            if day_of_week == 6 {
                sundays += 1;
            }
            // Skip to next month, taking special care around February.
            day_of_week += days;
            if *days == 28 {
                day_of_week += leap_day(y);
            }
        }
    }

    sundays
}

fn leap_day(year: u16) -> u16 {
    if year % 400 == 0 || (year % 4 == 0 && year % 100 != 0) {
        1
    } else {
        0
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn leap_day_1900() {
        assert_eq!(0, leap_day(1900));
    }

    #[test]
    fn leap_day_1904() {
        assert_eq!(1, leap_day(1904));
    }

    #[test]
    fn leap_day_2000() {
        assert_eq!(1, leap_day(2000));
    }
}
