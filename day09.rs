use std::fs;
use std::time::Instant;

fn part1(data: &str) -> i32 {
    let mut total_sum: i32 = 0;
    for line in data.lines() {
        let mut numbers: Vec<i32> = line.split(" ").map(|s| s.parse().unwrap()).collect();
        let mut current_nr: i32 = 0;

        while !numbers.iter().all(|i| *i == 0) {
            current_nr += numbers.last().unwrap();

            let mut new_numbers = vec![0; numbers.len() - 1];
            for i in 0..numbers.len() - 1 {
                new_numbers[i] = numbers[i + 1] - numbers[i];
            }
            numbers = new_numbers;
        }
        total_sum += current_nr;
    }
    return total_sum;
}

// Run with `rustc -O day09.rs && ./day09`
fn main() {
    let content = fs::read_to_string("inputs/day09.txt").expect("should read file");
    let before = Instant::now();
    let result = part1(&content);
    let elapsed = before.elapsed();
    println!("Result part 1: {result}, elapsed: {:?}", elapsed);
    assert!(result == 1974913025);
}
