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

fn part2(data: &str) -> usize {
    let mut boxes: Vec<Vec<(&str, usize)>> = vec![vec![]; 256];

    for part in data.trim_end().split(",") {
        if part.contains("-") {
            let lens = part.split("-").collect::<Vec<&str>>()[0];
            let idx: usize = hash(lens) as usize;
            // Remove box
            boxes[idx].retain(|&slot| !slot.0.eq(lens));
        } else if part.contains("=") {
            let parts: Vec<&str> = part.split('=').collect();
            let lens = parts[0];
            let value = parts[1].parse().unwrap();
            let idx: usize = hash(lens) as usize;
            let mut replaced = false;

            for i in 0..boxes[idx].len() {
                if boxes[idx][i].0 == lens {
                    boxes[idx][i] = (lens, value);
                    replaced = true;
                }
            }
            if !replaced {
                boxes[idx].push((lens, value));
            }
        }
    }

    let mut total_sum: usize = 0;
    for i in 0..boxes.len() {
        for (j, slot) in boxes[i].iter().enumerate() {
            total_sum += (i + 1) * (j + 1) * slot.1;
        }
    }
    return total_sum;
}

fn main() {
    let content = include_str!("../../inputs/day15.txt");
    let before = std::time::Instant::now();
    let result1 = part1(&content);
    assert_eq!(result1, 510273);
    // println!("Result part 1: {result1}");
    let result2 = part2(&content);
    assert_eq!(result2, 212449);
    // println!("Result part 2: {result2}");
    let elapsed = before.elapsed();
    println!("Day 15: {:?}", elapsed);
}
