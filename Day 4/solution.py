# Exercise 1

skills = ["Python", "SQL", "Excel"]

# 1. 
print(skills)
print(len(skills))

# 2.
first_index = skills[0]
last_index = skills[-1]

print(first_index)
print(last_index)

# 3.
skills.append("Power BI")
print(skills)

# 4.
skills.insert(1, "Git")
print(skills)

# Exercise 2
employee_ages = [24, 31, 28, 45, 19, 31]

# 1. 
print(28 in employee_ages)

# 2.
print(employee_ages.count(31))

# 3.
employee_ages.remove(31)
print(employee_ages)

# 4.
employee_ages.sort()
print(employee_ages)

employee_ages.reverse()
print(employee_ages)

# 5
print(employee_ages.index(45)) # Reversed

employee_ages.sort()
print(employee_ages.index(45)) # Sorted

# Exercise 3
employees = [
    ["Joshua", 21, "Backend"],
    ["Maria", 26, "Frontend"],
    ["Juan", 30, "Database"]
]

# 1.
print(employees[1])

# 2.
print(employees[2][2])

# 3.
last_pop = employees.pop()
print(last_pop)
print(employees)

# 4.
print(employees[:2])

# 5.
employees[1][2] = "Fullstack"
print(employees)