# Day 04 — Lists

## Topics covered (strictly Day 4 — no dicts/loops/comprehensions yet)
- Creating lists
- Indexing and slicing lists
- List methods: `.append()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`,
  `.reverse()`, `.count()`, `.index()`
- Checking membership with `in`
- Nested lists (a list containing lists)
- `len()` on lists

## Scenario
Today you graduate from single employee variables to your **first real
data structure** — a list of employee names/skills. Still no loops yet
(that's Day 9), so you'll interact with the list directly, one operation
at a time.

## Exercise 1 — Level 1 (Warm-up)
```python
skills = ["Python", "SQL", "Excel"]
```
1. Print the list, then print its length using `len()`.
2. Print the first and last items using indexing (use `-1` for last, don't
   hardcode the position number).
3. Add `"Power BI"` to the end of the list using `.append()`, print the
   result.
4. Insert `"Git"` at position `1` using `.insert()`, print the result.

## Exercise 2 — Level 2 (Modifying + membership)
```python
employee_ages = [24, 31, 28, 45, 19, 31]
```
1. Check if `28` is in the list using the `in` keyword, print the result
   (should be `True`).
2. Use `.count()` to find out how many times `31` appears.
3. Use `.remove()` to remove the **first occurrence** of `31`, print the
   list after.
4. Use `.sort()` to sort the list in ascending order, print it. Then use
   `.reverse()` on that same sorted list to flip it to descending, print
   again.
5. Use `.index()` to find the position of `45` in the current (sorted,
   reversed) list.

## Exercise 3 — Level 3 (Stretch — nested lists + slicing)
```python
employees = [
    ["Joshua", 21, "Backend"],
    ["Maria", 26, "Frontend"],
    ["Juan", 30, "Database"]
]
```
1. Print the second employee's full record (`employees[1]`).
2. Print just Juan's role by chaining indexes (`employees[?][?]`).
3. Use `.pop()` to remove the last employee from the `employees` list
   entirely, print what was removed and print the list after.
4. Use slicing to print only the **first two** remaining employees.
5. Bonus: change Maria's role from `"Frontend"` to `"Fullstack"` by
   directly reassigning that nested index (e.g.
   `employees[0][2] = "New Role"` pattern) — don't use `.replace()`,
   that's a string method, not a list method.
