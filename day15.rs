fn hash(s: &str) -> u32 {
    let mut current_value: u32 = 0;
    for c in s.chars() {
        current_value += c as u32;
        current_value *= 17;
        current_value %= 256;
    }
    return current_value;
}

fn part1(data: &str) -> u32 {
    let mut total_sum: u32 = 0;
    for part in data.trim_end().split(",") {
        total_sum += hash(part);
    }
    return total_sum;
}

// Run with `rustc -O day15.rs && ./day15`
fn main() {
    let content = include_str!("inputs/day15.txt");
    let before = std::time::Instant::now();
    let result = part1(&content);
    let elapsed = before.elapsed();
    println!("Result part 1: {result}, elapsed: {:?}", elapsed);
    assert_eq!(result, 510273);
}
