use std::collections::HashMap;
use std::time::Instant;

fn main() {
    // Variable declaration
    let nr: u32 = 4;
    let mut is_changed = true;
    println!("Nr: {nr}, is_changed: {:?}", is_changed);
    is_changed = false;
    let char = 'u';
    println!("Char 'u' as ascii: {:?}", char as usize);
    let exp: f32 = 3.2;
    let my_tuple = ("foo", 3);
    println!("First element of tuple: {:?}", my_tuple.0);

    // Timing, assertions
    let before = Instant::now();
    let result1 = nr.pow(2) + 5;
    assert_eq!(result1, 21);
    assert_ne!(exp, 2.3);
    let elapsed = before.elapsed();
    println!("Day 9: {:?}", elapsed);

    // Loops, conditionals
    let mut total_sum: usize = 0;
    for i in 3..5 {
        total_sum += i;
    }
    let mut a = 0;
    loop {
        if a == 0 {
            break;
        }
    }
    while a == 0 {
        a += if is_changed { 1 } else { 2 };
    }
    println!("Iteration, total_sum: {total_sum}, a: {a}");

    // String manipulation
    let my_str: &str = "Hello, Rust!";
    if !my_str.is_empty() {
        let is_equal = my_str.eq("test");
        let nr: i8 = "42".parse().unwrap();
        println!("is_equal: {is_equal}, parsed number: {nr}");
    }

    // Vectors, iteration, functional programming
    let mut empty_vec: Vec<usize> = Vec::new();
    empty_vec.push(3);
    empty_vec.push(4);
    empty_vec.remove(1);
    assert_eq!(empty_vec.len(), 1);
    let str_vec = "Hello\nWorld!".split('\n').collect::<Vec<_>>();
    let numbers: Vec<i32> = "1 2 3".split(" ").map(|s| s.parse().unwrap()).collect();
    println!("First and last: {:?}, {:?}", numbers.first().unwrap(), numbers.last().unwrap());

    let all_positive = numbers.iter().filter(|&n| n % 2 != 0).all(|&i| i == 0);
    println!("Filtered and checked if they match predicate: {:?}", all_positive);

    let skip_and_square: Vec<_> = numbers.iter().skip(1).map(|&n| n * 2).collect();
    println!("Skipped first number, squared the rest: {:?}", skip_and_square);

    for s in str_vec.iter() {
        println!("String part: {s}");
    }
    for (i, s) in str_vec.iter().rev().enumerate() {
        println!("String part {i}: {s}");
    }

    // TODO reference vs. value
    for n in numbers.iter() {
        let result = n + 3;
        println!("iter()-result: {result}");
    }
    for n in numbers.into_iter() {
        let result = n + 3;
        println!("into_iter()-result: {result}");
    }

    // HashMaps
    let mut length_hashmap: HashMap<&str, i32> = HashMap::new();
    length_hashmap.insert("foo", 3);
    length_hashmap.insert("foos", 4);

    let foo_len = length_hashmap.get("foo").unwrap();
    let hashmap_sum: i32 = length_hashmap.values().sum();
    println!("Hashmap: foo_len: {:?}, value sum: {:?}", foo_len, hashmap_sum);

    length_hashmap.clear();
    let has_bar = length_hashmap.contains_key("bar");
    println!("Hashmap has bar: {:?}", has_bar);

    let directions = HashMap::from([
        ("R", (0, 1)),
        ("L", (0, -1)),
        ("U", (-1, 0)),
        ("D", (1, 0)),
    ]);
    println!("'R' moves {:?}", directions["R"]);

    // TODO borrow/mutability
}
