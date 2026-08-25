# Day 02 — Operators

## Topics covered (strictly Day 2 — no lists/dicts/conditionals yet)
- Arithmetic operators: `+  -  *  /  //  %  **`
- Comparison operators: `==  !=  >  <  >=  <=`
- Logical operators: `and  or  not`
- Assignment operators: `=  +=  -=  *=  /=`
- Operator precedence (order of operations)

## Scenario
You're still working with single employee variables (no lists/dicts yet —
those come on Day 4 and Day 7). Today you calculate things about that
employee using operators.

## Exercise 1 — Level 1 (Warm-up)
Given:
```python
base_salary = 25000
bonus_rate = 0.10
years_of_service = 3
```
1. Calculate and print the `bonus` (`base_salary * bonus_rate`).
2. Calculate and print `total_pay` (`base_salary + bonus`).
3. Use `//` (floor division) and `%` (modulus) to find out how many full
   years and remaining months are in `years_of_service` if it were actually
   given in months instead (e.g. if `years_of_service_months = 40`, that's
   3 years and 4 months — practice this with 40).

## Exercise 2 — Level 2 (Comparison + Logical)
Given:
```python
age = 24
years_of_service = 3
performance_score = 8.5  # out of 10
```
1. Using comparison operators, check and print:
   - Is the employee at least 18 years old? (`age >= 18`)
   - Has the employee worked 5 years or more?
2. An employee qualifies for a raise if BOTH: `performance_score >= 7`
   AND `years_of_service >= 2`. Write this as one boolean expression using
   `and`, store it in a variable called `qualifies_for_raise`, and print it.
3. Print the **opposite** of `qualifies_for_raise` using `not`.

## Exercise 3 — Level 3 (Stretch — assignment operators + precedence)
1. Start with `salary = 20000`. Using `+=`, increase it by `1500`
   (don't rewrite the whole line as `salary = salary + 1500` — use the
   shorthand).
2. Using `*=`, apply a 5% raise to that same `salary` variable in place.
3. Predict on paper (write it as a comment) what this evaluates to, THEN
   run it and check if you were right:
   ```python
   result = 10 + 5 * 2 - 3 ** 2
   ```
4. Bonus: rewrite that same expression using parentheses so it evaluates
   to a **different** result than the original, and print both to compare.
