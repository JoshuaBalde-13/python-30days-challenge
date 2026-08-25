# Day 01 - Variables, Data Types & Built-in Functions
# Write your solutions below.

# ---- Exercise 1 ----
employee_name = "Joshua"
age = 20
salary = 50000.89
is_active = True

print(type(employee_name))
print(type(age))
print(type(salary))
print(type(is_active))

# ---- Exercise 2 ----
# 1.
print(len(employee_name))

# 2.
age_text = str(age)
print(employee_name + " is " + age_text + " years old" )
# or
print(f"{employee_name} is {age} years old")

# 3.
salary_int = int(salary)
print(salary_int) #This converted to a number only without a decimal 


# 4. 
print(f"Active status: {is_active}")

# ---- Exercise 3 ----
# 1.

age_input = input("Enter your age: ")

# 2.

age_converted = int(age_input)
print(age_converted)

# 3.

print(type(age_input))
print(type(age_converted))

# 4.

year_calculated = 2026 - age_converted
result = year_calculated
print(result)

