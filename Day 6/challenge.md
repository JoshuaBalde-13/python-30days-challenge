# Day 06 — Sets

## Topics covered (strictly Day 6 — no dicts/loops/comprehensions yet)
- Creating sets
- Sets are **unordered** and have **no duplicates**
- Set methods: `.add()`, `.remove()`, `.discard()`, `.pop()`, `.clear()`
- Set operations: union (`|`), intersection (`&`), difference (`-`),
  symmetric difference (`^`)
- Converting between `list` and `set` (handy for removing duplicates)
- Membership with `in`

## Scenario
Sets are perfect for de-duplicating data and comparing groups — like
finding which skills two employees have in common, or removing duplicate
entries from a messy dataset (a very real data-cleaning task).

## Exercise 1 — Level 1 (Warm-up)
```python
skills_joshua = {"Python", "SQL", "Excel", "Git"}
```
1. Print the set, then print its length using `len()`.
2. Add `"Power BI"` using `.add()`, print the result.
3. Remove `"Excel"` using `.discard()` (safer than `.remove()` — it won't
   error if the item isn't there), print the result.
4. Check membership: is `"SQL"` in the set? Print `True`/`False`.

## Exercise 2 — Level 2 (Set operations)
```python
skills_joshua = {"Python", "SQL", "Excel", "Git"}
skills_maria = {"SQL", "Excel", "Figma", "HTML"}
```
1. Find the skills **both** employees have using `&` (intersection),
   print it.
2. Find **all unique skills** across both employees combined using `|`
   (union), print it.
3. Find skills Joshua has that Maria does **not** have using `-`
   (difference), print it.
4. Find skills that are **only** in one set but not the other (not
   shared by both) using `^` (symmetric difference), print it.

## Exercise 3 — Level 3 (Stretch — deduplication + conversion)
```python
raw_ages = [24, 31, 28, 31, 24, 45, 19, 31]
```
1. This list has duplicate ages from messy data entry. Convert it to a
   set to automatically remove duplicates, print the result. (Note: sets
   are unordered, so the printed order may look scrambled — that's
   expected.)
2. Convert that deduplicated set back into a **list**, then sort it, and
   print the final clean sorted list.
3. Given two sets:
   ```python
   team_a = {"Joshua", "Maria", "Juan"}
   team_b = {"Maria", "Ana"}
   ```
   Use `.pop()` on a **copy** of `team_a` (so you don't destroy the
   original — hint: `team_a.copy()`) and print what got removed. Since
   sets are unordered, note that `.pop()` removes an *arbitrary* item, not
   a specific one.
