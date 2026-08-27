# Day 03 — Strings

## Topics covered (strictly Day 3 — no lists/dicts/loops yet)
- String indexing and slicing
- String methods: `.upper()`, `.lower()`, `.strip()`, `.replace()`,
  `.split()`, `.join()`, `.find()`, `.count()`
- f-strings (formatted string literals)
- String concatenation vs. f-strings
- Escape characters: `\n`, `\t`, `\"`

## Scenario
Still working with single employee variables — today all about
manipulating text.

## Exercise 1 — Level 1 (Warm-up)
```python
full_name = "  Joshua Balde  "
```
1. Print the string with whitespace removed (`.strip()`).
2. Print it fully uppercase, then fully lowercase.
3. Print the length of the *stripped* version using `len()`.
4. Using indexing, print just the first letter and just the last letter
   of the stripped name.

## Exercise 2 — Level 2 (Slicing + methods)
```python
email = "joshua.balde@gmail.com"
```
1. Use slicing to extract and print just the username part (before the
   `@`) — don't hardcode the position number, find `@` first using
   `.find()`, then slice up to that index.
2. Use `.split("@")` to split the email into two parts, and print both.
3. Use `.replace()` to change `"gmail.com"` to `"outlook.com"` in the
   original email, print the result.
4. Check with `.count()` how many times the letter `"a"` appears in
   `full_name` from Exercise 1 (stripped version).

## Exercise 3 — Level 3 (Stretch — f-strings + join)
1. Given:
   ```python
   skills = "Python-SQL-Excel"
   ```
   Split this into a list using `.split("-")`, then use `.join()` to
   combine them back together separated by `", "` instead (result should
   read like `"Python, SQL, Excel"`).
2. Build a multi-line employee summary using an f-string and `\n` escape
   characters, e.g.:
   ```
   Name: Joshua Balde
   Email: joshua.balde@gmail.com
   Skills: Python, SQL, Excel
   ```
   (all in a single f-string using `\n` to break lines)
3. Bonus: print the summary with tab characters (`\t`) instead of spaces
   aligning the labels, e.g. `Name:\tJoshua Balde`.
