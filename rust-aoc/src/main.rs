// Add days here so IntelliJ is happy
mod day09;
mod day15;

use std::process::Command;

// Run day: Replace day in Cargo.toml and run "cargo run --release"
// Direct compile: `rustc -O day09.rs && ./day09`

// TODO below not working yet
// From https://github.com/clearlyMine/advent_rust/blob/2e6b6bd1950318973ba0ee9996fa9175868f42ec/year_2023/src/main.rs
fn main() {
    for i in 9..=25 {
        let cmd = Command::new("cargo")
            .args(["run", "--release", "--bin", format!("day{:02}", i).as_str()])
            .output()
            .unwrap();
        let output = String::from_utf8(cmd.stdout).unwrap();
        if output.is_empty() {
            break;
        }
        println!("Day {:02}", i);
        println!("{}", output);
    }
}
