# Day 08 — Conditionals

## Topics covered (strictly Day 8 — no loops yet, that's Day 9)
- `if`, `elif`, `else`
- Comparison and logical operators inside conditions (review from Day 2)
- Nested conditionals
- Truthy/falsy values (what counts as "True" without being literally `True`)
- Ternary (conditional) expressions — one-line if/else

## Scenario
Now that you know dictionaries, today's exercises use a single employee
dict and make decisions about it based on its values.

## Exercise 1 — Level 1 (Warm-up)
```python
employee = {"name": "Joshua", "age": 21, "salary": 25000}
```
1. Write an `if/else` that prints `"Adult"` if `employee["age"]` is 18 or
   over, otherwise prints `"Minor"`.
2. Write an `if/elif/else` that checks `employee["salary"]` and prints:
   - `"Low income"` if salary is below 20000
   - `"Mid income"` if salary is 20000–39999
   - `"High income"` if salary is 40000 or above
3. Check if `"email"` is a key in `employee` (like Day 7). If it's NOT
   present, print `"Missing email"`.

## Exercise 2 — Level 2 (Logical operators + nested conditionals)
```python
employee = {"name": "Maria", "age": 26, "years_of_service": 4, "performance_score": 8.2}
```
1. Write a single `if` condition using `and` that prints `"Eligible for
   raise"` only if `performance_score >= 7` AND `years_of_service >= 2`.
   Otherwise print `"Not eligible yet"`.
2. Write a **nested** conditional: first check if `age >= 18`. If true,
   *inside* that block, check if `years_of_service >= 3` and print
   `"Senior adult employee"` if so, otherwise print `"Junior adult
   employee"`. If the outer age check fails, print `"Underage — invalid
   record"`.
3. Using `or`, print `"Needs review"` if EITHER `performance_score < 5`
   OR `years_of_service < 1`. Otherwise print `"No review needed"`.

## Exercise 3 — Level 3 (Stretch — truthy/falsy + ternary)
1. Given `bio = ""` (an empty string) and `skills = []` (an empty list),
   write an `if` that checks `if bio:` directly (no `== ""` comparison)
   and prints `"Bio missing"` if it's empty. Do the same for `skills`
   with `"No skills listed"`. As a comment, explain in your own words why
   an empty string/list evaluates as falsy without needing `== ""`.
2. Given `salary = 0`, write `if salary:` directly and observe what
   happens — as a comment, note whether `0` is treated as truthy or
   falsy, and why this could actually cause a **bug** if `0` were a
   legitimately valid salary value in real data.
3. Rewrite Exercise 1's #1 (Adult/Minor check) as a **one-line ternary
   expression** instead of a full if/else block:
   ```python
   status = "Adult" if employee["age"] >= 18 else "Minor"
   ```
   Print `status`.
