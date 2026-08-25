# Day 01 — Variables, Data Types & Built-in Functions

## Topics covered (strictly Day 1 — no lists/dicts yet, those come later)
- Variables and naming
- Core data types: `int`, `float`, `str`, `bool`
- Type checking with `type()`
- Type conversion: `int()`, `str()`, `float()`
- Built-in functions: `print()`, `len()`, `type()`, `input()`

## Scenario
You're logging basic info for a single employee, one field at a time —
just plain variables, no data structures yet.

## Exercise 1 — Level 1 (Warm-up)
Create these variables:
- `employee_name` (string)
- `age` (int)
- `salary` (float)
- `is_active` (bool)

Print each one, and print its type using `type()`.

## Exercise 2 — Level 2
1. Using `len()`, print how many characters are in `employee_name`.
2. Convert `age` to a string and build a sentence using string
   concatenation: `"Joshua is 21 years old"`.
3. Convert `salary` (float) to an `int` using `int()` and print the result.
   What happens to the decimal part? Add a comment explaining what you
   observe.
4. Take `is_active` and print it inside a sentence, e.g.
   `"Active status: True"`.

## Exercise 3 — Level 3 (Stretch)
1. Use `input()` to ask the user to type their age (input always returns
   a string). Store it in a variable called `age_input`.
2. Convert `age_input` to an `int` using `int()`.
3. Print the type of `age_input` *before* conversion, and the type
   *after* conversion — prove to yourself it actually changed.
4. Bonus: calculate and print what year the person was born, using the
   converted age and a reasonable current year (you can hardcode the
   current year as a variable).
git commit -m "Day 01: variables, data types, built-in functions"
git push
\`\`\`
