# Day 09 — Loops

## Topics covered (strictly Day 9 — no functions/comprehensions yet)
- `for` loops — over lists, strings, dicts, and `range()`
- `while` loops
- `break` and `continue`
- Looping with `.items()`, `.keys()`, `.values()` (dicts)
- Nested loops
- Combining loops with conditionals (Day 8)

## Scenario
This is the day everything from Days 1–8 finally clicks together — no
more typing `raw_salary1`, `raw_salary2`... by hand. Loops let you
process *any* amount of data with the same few lines.

## Exercise 1 — Level 1 (Warm-up — basic `for` loops)
```python
skills = ["Python", "SQL", "Excel", "Power BI"]
```
1. Loop through `skills` and print each one.
2. Loop through `skills` using `enumerate()` and print each item with its
   position, like `"1: Python"`, `"2: SQL"` (remember `enumerate()` starts
   at 0 by default — add 1 when printing).
3. Use a `for` loop with `range(1, 6)` to print numbers 1 through 5.

## Exercise 2 — Level 2 (Loops + conditionals combined)
```python
employees = [
    {"name": "Joshua", "salary": 25000},
    {"name": "Maria", "salary": 45000},
    {"name": "Juan", "salary": 18000},
    {"name": "Ana", "salary": 52000}
]
```
1. Loop through `employees` and print each employee's name and salary.
2. Inside the same loop, use an `if` to print `"High earner"` next to
   anyone with `salary >= 40000`, otherwise print `"Standard"`.
3. Keep a running total using a variable initialized to `0` **before**
   the loop, adding each employee's salary inside the loop. After the
   loop ends, print the total combined salary.
4. Use `continue` to **skip** printing anyone with salary below `20000`
   — print everyone else's name normally.

## Exercise 3 — Level 3 (Stretch — while, break, nested loops, dict looping)
1. Write a `while` loop that starts a `countdown = 5` and prints each
   number down to `1`, then prints `"Liftoff!"` after the loop ends.
2. Given `attempts = [12, 45, 7, 89, 34, 6]`, use a `for` loop with
   `break` to stop looping the moment you find a number greater than
   `50`, and print that number.
3. Loop through this dictionary using `.items()` and print each key-value
   pair as `"role: count"`:
   ```python
   team_counts = {"Backend": 3, "Frontend": 2, "Database": 1}
   ```
4. Write a **nested loop**: for each employee in `employees` (from
   Exercise 2), loop through a fixed list `bonus_tiers = ["Q1", "Q2",
   "Q3", "Q4"]` and print `"Joshua - Q1 bonus check"` style lines for
   every employee/quarter combination (should print 16 lines total: 4
   employees × 4 quarters).
