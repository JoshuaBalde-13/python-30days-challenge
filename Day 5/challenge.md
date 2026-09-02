# Day 05 — Tuples

## Topics covered (strictly Day 5 — no dicts/sets/loops yet)
- Creating tuples
- Tuples are **immutable** (can't be changed after creation)
- Indexing and slicing tuples (same as lists)
- Tuple packing and unpacking
- Tuple methods: `.count()`, `.index()`
- Converting between `list` and `tuple`
- When to use a tuple vs. a list

## Scenario
Tuples are perfect for data that shouldn't change — like a fixed
coordinate, a fixed date, or a record that represents a single fixed
"snapshot" of something. Today's exercises use employee records that are
meant to stay fixed.

## Exercise 1 — Level 1 (Warm-up)
```python
employee_record = ("Joshua", 21, "Backend")
```
1. Print the tuple, then print its length using `len()`.
2. Print the first and last items using indexing.
3. Try to change the role (index `2`) to `"Fullstack"` by direct
   assignment (`employee_record[2] = "Fullstack"`). Run it, and as a
   comment, write down the exact error Python gives you and why it
   happens.

## Exercise 2 — Level 2 (Unpacking + methods)
```python
coordinates = (14.5995, 120.9842, "Manila")
```
1. **Unpack** the tuple into three separate variables in one line:
   `latitude, longitude, city = coordinates`. Print all three.
2. Given `scores = (8, 9, 7, 9, 10, 9)`, use `.count()` to find how many
   times `9` appears.
3. Use `.index()` to find the position of the first `10` in `scores`.
4. Check membership: is `7` in `scores`? Print `True`/`False` using `in`.

## Exercise 3 — Level 3 (Stretch — packing, conversion, nested tuples)
1. Create a tuple **without parentheses** (tuple packing) holding three
   skill names, e.g. `skills = "Python", "SQL", "Excel"`. Print it and
   print `type(skills)` to prove it's really a tuple.
2. Convert `skills` into a list using `list()`, add `"Power BI"` to that
   list with `.append()` (since tuples can't be appended to directly),
   then convert it back into a tuple using `tuple()`. Print the final
   result.
3. Create a **nested tuple** of 3 employees, each themselves a tuple:
   ```python
   employees = (
       ("Joshua", 21, "Backend"),
       ("Maria", 26, "Frontend"),
       ("Juan", 30, "Database")
   )
   ```
   Print Juan's role by chaining indexes.
4. Bonus (short written answer, as a comment in your code): in your own
   words, when would you choose a tuple over a list in a real data
   project? Give one concrete example.
