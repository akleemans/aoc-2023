fn count_ways(times: Vec<usize>, distances: Vec<usize>) -> usize {
    let mut total_ways: usize = 1;
    for i in 0..times.len() {
        let t = times[i];
        let d = distances[i];
        let mut sum: usize = 0;
        for j in 0..t {
            if j * (t - j) > d {
                sum += 1;
            }
        }
        total_ways *= sum;
    }
    return total_ways;
}

fn split_to_ints(s: &str) -> Vec<usize> {
    return s.split_whitespace().collect::<Vec<&str>>().iter().skip(1).map(|el| el.parse().unwrap()).collect();
}

fn part1(data: &str) -> usize {
    let parts = data.split('\n').collect::<Vec<&str>>();
    let times = split_to_ints(parts[0]);
    let distances = split_to_ints(parts[1]);
    return count_ways(times, distances);
}

fn split_part2(s: &str) -> Vec<usize> {
    return s.replace(" ", "").as_str().split(":").collect::<Vec<&str>>().iter().skip(1).map(|el| el.parse().unwrap()).collect();
}


fn part2(data: &str) -> usize {
    let parts = data.split('\n').collect::<Vec<&str>>();
    let times: Vec<usize> = split_part2(parts[0]);
    let distances = split_part2(parts[1]);
    return count_ways(times, distances);
}

fn main() {
    let content = include_str!("../../inputs/day06.txt");
    let before = std::time::Instant::now();
    let result1 = part1(&content);
    assert_eq!(result1, 1083852);
    // println!("Result part 1: {result1}");
    let result2 = part2(&content);
    assert_eq!(result2, 23501589);
    // println!("Result part 2: {result2}");
    let elapsed = before.elapsed();
    println!("Day 6: {:?}", elapsed);
}
