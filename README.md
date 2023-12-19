# aoc-2023

My solution for [Advent of Code 2023](https://adventofcode.com/2023) in Python 3.

## Execution times

All code in Python/[Codon](https://docs.exaloop.io/codon), some days also in Rust.

* Python: 3.12 - `python3 run_python.py`
* Codon: 0.16.3 - `python3 run_codon.py`
* Rust: 1.74.1 - `cargo run --release`

| Day    | Python   | Codon    | Rust   |
|--------|----------|----------|--------|
| Day 1  | 76.7ms   | 23.2ms   |        |
| Day 2  | 28.2ms   | 4.0ms    |        |
| Day 3  | 68.7ms   | 8.2ms    |        |
| Day 4  | 36.5ms   | 5.4ms    |        |
| Day 5  | ?        | 4711.2ms |        |
| Day 6  | 2989.3ms | 363.9ms  | 21.3ms |
| Day 7  | 50.5ms   | 12.0ms   |        |
| Day 8  | 144.2ms  | -        |        |
| Day 9  | 40.4ms   | 5.0ms    | 505µs  |
| Day 10 | 80.6ms   | 13.5ms   |        |
| Day 11 | 1182.6ms | 89.0ms   |        |
| Day 12 | 400.3ms  | -        |        |
| Day 13 | 286.5ms  | 35.9ms   |        |
| Day 14 | 4392.7ms | 390.7ms  |        |
| Day 15 | 51.8ms   | 4.5ms    | 590µs  |
| Day 16 | 2518.1ms | 516.9ms  |        |
| Day 17 |          |          |        |
| Day 18 |          |          |        |

## Learned along the way

### Rust!

See `rust-aoc/src/learn.rs` and Rust days.

### Python: Memoize using `@cache` (Day 12)

For Dynamic Programming problems, it can be useful to memoize function results.
Especially for recursive functions, it means that a whole branch can be skipped, as we can look up the result (if we
calculated it already before).

```python
from functools import cache


@cache
def place_next(state: str, groups) -> int:
    ...
```

Note: `list`s can not be used as function parameters, but they can be converted to `tuple()`.


