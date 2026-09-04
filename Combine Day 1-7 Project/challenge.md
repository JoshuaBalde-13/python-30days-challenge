# Checkpoint — Days 1–7 Combined Project

## Constraint
No `if/else` and no loops yet (those start Day 8 and Day 9) — every task
below must be solved using only what you've learned so far: variables,
data types, operators, strings, lists, tuples, sets, and dictionaries.
This is intentional — it forces you to actually combine the tools instead
of reaching for a loop as a shortcut.

## Scenario
You're building a tiny "employee records" mini-system, entirely by hand,
using the structures you've learned so far. Think of this as a rough
first draft of what a real HR data record might look like before you
know how to automate it with loops.

## Part 1 — Build a single employee record (Days 1–3: variables, types, strings)
1. Create individual variables for one employee: `full_name` (with extra
   whitespace around it, like `"  Joshua Balde  "`), `age` (int),
   `salary` (float), `is_active` (bool).
2. Clean `full_name` using `.strip()`, then get just the first name using
   `.split()` and indexing (hint: `full_name.strip().split(" ")[0]`).
3. Build an f-string summary sentence combining `full_name`, `age`, and
   `salary`, e.g. `"Joshua Balde is 21 years old, earning 25000.0"`.
4. Calculate a 10% bonus using arithmetic operators (Day 2), and print
   `total_pay` (`salary + bonus`).

## Part 2 — Structure it properly (Days 4, 5, 7: lists, tuples, dicts)
1. Take the individual variables from Part 1 and combine them into a
   **dictionary** called `employee` with keys: `name`, `age`, `salary`,
   `is_active`.
2. Create a **tuple** called `employee_id` holding a fixed, unchangeable
   pair: `("E001", "2024-01-15")` (id number, hire date — data that
   shouldn't change).
3. Create a **list** called `skills` with at least 4 skills.
4. Add `skills` and `employee_id` as new keys inside the `employee`
   dictionary, so the dictionary now fully represents one employee with
   nested data.

## Part 3 — Compare two employees (Days 6, 7: sets, dicts)
1. Create a second employee dictionary, `employee_2`, following the same
   structure as Part 2, with its own different skills list.
2. Convert both employees' `skills` lists into **sets**, then use set
   operations to find:
   - Skills both employees share (`&`)
   - Skills unique to `employee` only (`-`)
3. Using `.get()`, safely check if `employee_2` has a `"bonus"` key (it
   won't) and print a default message instead of crashing.

## Part 4 — Clean messy data (Days 1, 6: type conversion, sets)
```python
raw_salaries = ["25000", "27000", "25000", "31000", "27000"]
```
1. These came in as strings (common in real messy data, e.g. from a CSV).
   Convert each one to a float — since you don't have loops yet, do this
   manually one at a time using `float()`, OR discover and try Python's
   `list(map(float, raw_salaries))` as a preview of a technique you'll
   fully learn later. Either is fine — try the manual way first, then try
   `map()` if you're curious.
2. Convert the cleaned list to a **set** to see the unique salary values,
   print it.

## Part 5 — Final printout
Print a clean, multi-line summary of `employee` using an f-string and
`\n`, showing name, age, salary, total pay, skills, and employee ID —
pulling every value **from the dictionary itself**, not from the original
loose variables.
