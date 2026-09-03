# Day 07 — Dictionaries

## Topics covered (strictly Day 7 — no loops/comprehensions yet)
- Creating dictionaries (key-value pairs)
- Accessing, adding, and updating values
- Dictionary methods: `.keys()`, `.values()`, `.items()`, `.get()`,
  `.update()`, `.pop()`
- Checking membership with `in` (checks **keys** by default)
- Nested dictionaries
- Converting between structures (e.g. `.items()` back to a list of tuples)

## Scenario
This is the data structure you'll use constantly in real data/backend
work — representing a single record (like one employee, one API response
object) as labeled fields instead of just an ordered list.

## Exercise 1 — Level 1 (Warm-up)
```python
employee = {"name": "Joshua", "age": 21, "role": "Backend"}
```
1. Print the dictionary, then print its length using `len()`.
2. Access and print the `"name"` value using square-bracket syntax
   (`employee["name"]`).
3. Add a new key `"salary"` with value `25000` to the dictionary. Print
   the updated dictionary.
4. Update the `"role"` value to `"Fullstack"`. Print the updated
   dictionary.

## Exercise 2 — Level 2 (Safe access + methods)
```python
employee = {"name": "Joshua", "age": 21, "role": "Backend", "salary": 25000}
```
1. Use `.get("email")` to try accessing a key that doesn't exist. Print
   the result — notice it doesn't crash like `employee["email"]` would.
2. Use `.get("email", "Not provided")` this time, with a default value,
   and print it.
3. Print all the keys using `.keys()`, all the values using `.values()`,
   and all the key-value pairs using `.items()`.
4. Check membership: is `"role"` a key in the dictionary? Print
   `True`/`False` using `in`.

## Exercise 3 — Level 3 (Stretch — nested dicts + update/pop)
```python
employees = {
    "E001": {"name": "Joshua", "role": "Backend", "salary": 25000},
    "E002": {"name": "Maria", "role": "Frontend", "salary": 27000}
}
```
1. Print Joshua's role by chaining keys: `employees["E001"]["role"]`.
2. Add a **third** employee record `"E003"` with your own made-up
   name/role/salary, using direct key assignment (not `.update()` yet).
3. Use `.update()` to change `E002`'s salary to `30000` — remember
   `.update()` takes a dictionary, so you'll do something like
   `employees["E002"].update({"salary": 30000})`. Print the result.
4. Use `.pop("E001")` to remove Joshua's entire record from `employees`,
   print what was removed (`.pop()` returns it, just like with lists) and
   print the dictionary after.
5. Bonus (short written comment): what's one advantage a dictionary has
   over a list when representing a single employee record, and one
   disadvantage?
