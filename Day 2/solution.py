#Given 

base_salary = 25000
bonus_rate = 0.10
years_of_service = 3

#Exercise 1 
# 1.
bonus = (base_salary * bonus_rate)
print(bonus)

# 2.
total_pay = (base_salary * bonus)
print(total_pay)

# 3.
years_of_service_months = 40

full_years = (years_of_service_months // 12)
remaining_months = (years_of_service_months % 12)

print(f"The full year is {full_years} years and the remaining months is {remaining_months} months")

#Exercise 2

#Given
age = 24
years_of_service = 3
performance_score = 8.5  # out of 10

# 1.
print(age >= 18)
print(years_of_service >= 5)

# 2.
qualifies_for_raise = (performance_score >= 7 and years_of_service >= 2)
print(qualifies_for_raise)

opposite_qualifies_for_raise = not (performance_score >=7 and years_of_service >= 2)

# 3.
print(opposite_qualifies_for_raise)

# Exercise 3

# 1.
salary = 20000
salary += 1500

# 2.
salary *= 1.05
print(salary)

# 3.
result = 10 + 5 * 2 - 3 ** 2
print(result)





