fn solve(data: &str, backwards: bool) -> i32 {
    let mut total_sum: i32 = 0;
    for line in data.lines() {
        let mut numbers: Vec<i32> = line.split(" ").map(|s| s.parse().unwrap()).collect();
        let mut current_nr: i32 = 0;
        let mut mult: i32 = 1;

        while !numbers.iter().all(|i| *i == 0) {
            current_nr += mult * if backwards { numbers.first().unwrap() } else { numbers.last().unwrap() };
            mult *= if backwards { -1 } else { 1 };

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

fn main() {
    let content = include_str!("../../inputs/day09.txt");
    let before = std::time::Instant::now();
    let result1 = solve(&content, false);
    assert_eq!(result1, 1974913025);
    // println!("Result part 1: {result1}");
    let result2 = solve(&content, true);
    assert_eq!(result2, 884);
    // println!("Result part 2: {result2}");
    let elapsed = before.elapsed();
    println!("Day 9: {:?}", elapsed);
}
