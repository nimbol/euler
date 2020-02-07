/// # Largest product in a grid
/// In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
/// ```text
/// 08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
/// 49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
/// 81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
/// 52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
/// 22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
/// 24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
/// 32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
/// 67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
/// 24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
/// 21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
/// 78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
/// 16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
/// 86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
/// 19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
/// 04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
/// 88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
/// 04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
/// 20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
/// 20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
/// 01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
/// ```
/// The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
///
/// What is the greatest product of four adjacent numbers in the same direction
/// (up, down, left, right, or diagonally) in the 20×20 grid?
fn main() {
    let elements = vec![
        08, 02, 22, 97, 38, 15, 00, 40, 00, 75, 04, 05, 07, 78, 52, 12, 50, 77, 91, 08, 49, 49, 99,
        40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 04, 56, 62, 00, 81, 49, 31, 73, 55, 79,
        14, 29, 93, 71, 40, 67, 53, 88, 30, 03, 49, 13, 36, 65, 52, 70, 95, 23, 04, 60, 11, 42, 69,
        24, 68, 56, 01, 32, 56, 71, 37, 02, 36, 91, 22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54,
        22, 40, 40, 28, 66, 33, 13, 80, 24, 47, 32, 60, 99, 03, 45, 02, 44, 75, 33, 53, 78, 36, 84,
        20, 35, 17, 12, 50, 32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38,
        64, 70, 67, 26, 20, 68, 02, 62, 12, 20, 95, 63, 94, 39, 63, 08, 40, 91, 66, 49, 94, 21, 24,
        55, 58, 05, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72, 21, 36, 23, 09,
        75, 00, 76, 44, 20, 45, 35, 14, 00, 61, 33, 97, 34, 31, 33, 95, 78, 17, 53, 28, 22, 75, 31,
        67, 15, 94, 03, 80, 04, 62, 16, 14, 09, 53, 56, 92, 16, 39, 05, 42, 96, 35, 31, 47, 55, 58,
        88, 24, 00, 17, 54, 24, 36, 29, 85, 57, 86, 56, 00, 48, 35, 71, 89, 07, 05, 44, 44, 37, 44,
        60, 21, 58, 51, 54, 17, 58, 19, 80, 81, 68, 05, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77,
        04, 89, 55, 40, 04, 52, 08, 83, 97, 35, 99, 16, 07, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98,
        66, 88, 36, 68, 87, 57, 62, 20, 72, 03, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69, 04, 42,
        16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 08, 46, 29, 32, 40, 62, 76, 36, 20, 69, 36, 41, 72,
        30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 04, 36, 16, 20, 73, 35, 29, 78, 31, 90, 01,
        74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 05, 54, 01, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33,
        48, 61, 43, 52, 01, 89, 19, 67, 48,
    ];
    println!("{}", solve(elements, 4));
}

fn solve(elements: Vec<u64>, window_size: usize) -> u64 {
    let grid = Grid::new(elements).expect("Abort: invalid grid size");
    let windows = grid
        .windows(window_size)
        .expect("Abort: invalid window size");
    windows
        .iter()
        .map(|v| v.iter().product())
        .max()
        .expect("Abort: no windows")
}

#[derive(Debug, Clone)]
struct InvalidGridSizeError {}

#[derive(Debug, Clone)]
enum WindowError {
    OutOfBounds,
    TooLarge,
    TooSmall,
}

#[derive(Debug, Clone)]
struct Grid {
    dim: usize,
    elements: Vec<u64>,
}
impl Grid {
    pub fn new(elements: Vec<u64>) -> Result<Grid, InvalidGridSizeError> {
        let dim = match (elements.len() as f64).sqrt() as usize {
            size if size.pow(2) == elements.len() => Ok(size),
            _ => Err(InvalidGridSizeError {}),
        }?;
        Ok(Grid { dim, elements })
    }

    fn validate_window_size(&self, size: usize) -> Result<(), WindowError> {
        if size == 0 {
            return Err(WindowError::TooSmall);
        }
        if size > self.dim {
            return Err(WindowError::TooLarge);
        }
        Ok(())
    }

    fn validate_window_bounds(
        &self,
        size: usize,
        start: usize,
        hstep: isize,
        vstep: isize,
    ) -> Result<(), WindowError> {
        let size = size as isize;
        let (x, y) = ((start % self.dim) as isize, (start / self.dim) as isize);
        let dim = self.dim as isize;
        if !(0..dim).contains(&(x + (size - 1) * hstep)) {
            return Err(WindowError::OutOfBounds);
        }
        if !(0..dim).contains(&(y + (size - 1) * vstep)) {
            return Err(WindowError::OutOfBounds);
        }
        Ok(())
    }

    /// Get a window (`Vec<u64>`) of size `size` starting at position `start` in the grid.
    /// Use `hstep` and `vstep` to indicate window direction.
    fn window(
        &self,
        size: usize,
        start: usize,
        hstep: isize,
        vstep: isize,
    ) -> Result<Vec<u64>, WindowError> {
        self.validate_window_bounds(size, start, hstep, vstep)?;
        let step = hstep + vstep * self.dim as isize;
        let indices: Vec<isize> = (0..size as isize)
            .map(|n| start as isize + n * step)
            .collect();
        if indices
            .iter()
            .any(|&i| i < 0 || i as usize >= self.elements.len())
        {
            Err(WindowError::OutOfBounds)
        } else {
            Ok(indices.iter().map(|&i| self.elements[i as usize]).collect())
        }
    }

    pub fn windows(&self, size: usize) -> Result<Vec<Vec<u64>>, WindowError> {
        self.validate_window_size(size)?;
        let mut result = vec![];
        result.append(
            &mut (0..self.elements.len())
                .filter_map(|i| self.window(size, i, 1, 0).ok())
                .collect::<Vec<_>>(),
        );
        result.append(
            &mut (0..self.elements.len())
                .filter_map(|i| self.window(size, i, 1, 1).ok())
                .collect::<Vec<_>>(),
        );
        result.append(
            &mut (0..self.elements.len())
                .filter_map(|i| self.window(size, i, 0, 1).ok())
                .collect::<Vec<_>>(),
        );
        result.append(
            &mut (0..self.elements.len())
                .filter_map(|i| self.window(size, i, -1, 1).ok())
                .collect::<Vec<_>>(),
        );
        Ok(result)
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn windows_ok() {
        let grid = Grid::new(vec![1, 2, 3, 4]).unwrap();
        assert_eq!(
            vec![
                vec![1, 2],
                vec![3, 4],
                vec![1, 4],
                vec![1, 3],
                vec![2, 4],
                vec![2, 3],
            ],
            grid.windows(2).unwrap()
        );
    }
    #[test]
    fn window_horizontal_ok() {
        let grid = Grid::new(vec![7, 8, 9, 4, 5, 6, 3, 2, 1]).unwrap();
        assert_eq!(vec![7, 8, 9], grid.window(3, 0, 1, 0).unwrap());
        assert_eq!(vec![4, 5, 6], grid.window(3, 3, 1, 0).unwrap());
        assert_eq!(vec![3, 2, 1], grid.window(3, 6, 1, 0).unwrap());
        assert_eq!(vec![2, 1], grid.window(2, 7, 1, 0).unwrap());
    }
    #[test]
    #[should_panic]
    fn window_horizontal_err() {
        let grid = Grid::new(vec![7, 8, 9, 4, 5, 6, 3, 2, 1]).unwrap();
        grid.window(3, 1, 1, 0).unwrap();
    }
    #[test]
    fn window_vertical_ok() {
        let grid = Grid::new(vec![7, 8, 9, 4, 5, 6, 3, 2, 1]).unwrap();
        assert_eq!(vec![7, 4, 3], grid.window(3, 0, 0, 1).unwrap());
        assert_eq!(vec![8, 5, 2], grid.window(3, 1, 0, 1).unwrap());
        assert_eq!(vec![9, 6, 1], grid.window(3, 2, 0, 1).unwrap());
        assert_eq!(vec![5, 2], grid.window(2, 4, 0, 1).unwrap());
    }
    #[test]
    #[should_panic]
    fn window_vertical_err() {
        let grid = Grid::new(vec![7, 8, 9, 4, 5, 6, 3, 2, 1]).unwrap();
        grid.window(3, 3, 0, 1).unwrap();
    }
    #[test]
    fn window_diagonal_nwse_ok() {
        let grid = Grid::new(vec![7, 8, 9, 4, 5, 6, 3, 2, 1]).unwrap();
        assert_eq!(vec![7, 5, 1], grid.window(3, 0, 1, 1).unwrap());
        assert_eq!(vec![8, 6], grid.window(2, 1, 1, 1).unwrap());
    }
    #[test]
    fn window_diagonal_nesw_ok() {
        let grid = Grid::new(vec![7, 8, 9, 4, 5, 6, 3, 2, 1]).unwrap();
        assert_eq!(vec![9, 5, 3], grid.window(3, 2, -1, 1).unwrap());
        assert_eq!(vec![8, 4], grid.window(2, 1, -1, 1).unwrap());
    }
    #[test]
    fn new_dimension_valid() {
        Grid::new(vec![1]).unwrap();
        Grid::new(vec![1, 2, 3, 4]).unwrap();
        Grid::new(vec![1, 2, 3, 4, 5, 6, 7, 8, 9]).unwrap();
        Grid::new(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]).unwrap();
    }
    #[test]
    #[should_panic]
    fn get_dimension_invalid() {
        Grid::new(vec![1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).unwrap();
    }

    #[test]
    fn solve_horizontal() {
        assert_eq!(99 * 49, solve(vec![8, 2, 22, 49, 49, 99, 81, 49, 31], 2));
    }
    #[test]
    fn solve_vertical() {
        assert_eq!(99 * 77, solve(vec![11, 22, 99, 88, 66, 77, 33, 44, 55], 2));
    }
    #[test]
    fn solve_diagonal_nesw() {
        assert_eq!(99 * 77, solve(vec![11, 22, 99, 55, 77, 66, 99, 44, 88], 2));
    }
    #[test]
    fn solve_diagonal_nwse() {
        assert_eq!(99 * 77, solve(vec![88, 22, 33, 44, 77, 66, 88, 44, 99], 2));
    }
}
