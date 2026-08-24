# Day 01 — Variables, Data Types & Built-in Functions

## Topics covered
- Variables and naming
- Core data types: `int`, `float`, `str`, `bool`, `list`, `dict`, `tuple`, `set`
- Type checking with `type()`
- Basic built-in functions: `print()`, `len()`, `type()`, `int()`, `str()`, `float()`

## Scenario

You're building the very first piece of your future data toolkit: a record
for a single employee (yes — tying it back to your HRIS thesis theme).

## Exercise 1 — Level 1 (Warm-up)
Create variables for a single employee:
- `employee_name` (string)
- `age` (int)
- `salary` (float)
- `is_active` (bool)
- `skills` (list of strings, at least 3)

Print each variable and its type using `type()`.

## Exercise 2 — Level 2
1. Create a `dict` called `employee` that bundles all the info from Exercise 1
   into key-value pairs (`name`, `age`, `salary`, `is_active`, `skills`).
2. Print the dictionary.
3. Print only the employee's `skills` list from the dictionary.
4. Use `len()` to print how many skills the employee has.

## Exercise 3 — Level 3 (Stretch)
1. Create a `list` of **three** employee dictionaries (reuse the structure
   above with different data).
2. Loop through the list and print each employee's name and salary in the
   format: `"Juan Dela Cruz earns 25000.0"`
3. Calculate and print the **total combined salary** of all three employees
   (don't use pandas yet — just built-in Python).
4. Bonus: convert one employee's `age` (int) to a `str` and concatenate it
   into a sentence, e.g. `"Juan is 28 years old"`.
