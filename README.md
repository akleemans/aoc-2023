# aoc-2023

My solution for [Advent of Code 2023](https://adventofcode.com/2023) in Python 3.

## Execution times

All code in Python/[Codon](https://docs.exaloop.io/codon).
Timed with Codon 0.16.3: `python3 run_codon.py`

| Day    | Time    |
|--------|---------|
| Day 1  | 0.023s  |
| Day 2  | 0.004s  |
| Day 3  | 0.007s  |
| Day 4  | 0.007s  |
| Day 5  | 4.969s  |
| Day 6  | 0.361s  |
| Day 7  | 0.009s  |
| Day 8  | 0.080s* |
| Day 9  | 0.004s  |
| Day 10 | 0.005s  |
| Day 11 | 0.063s  |
| Day 12 | 0.258s* |
| Day 13 | 0.035s  |
| Day 14 | 0.374s  |
| Day 15 |         |
| Day 16 |         |
| Day 17 |         |
| Day 18 |         |

* = Not compiled to Codon yet

## Learned along the way

### Memoize using `func` (Day 12)

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


