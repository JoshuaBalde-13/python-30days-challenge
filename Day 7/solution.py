# Day 07 - Dictionaries
# Write your solutions below.

# ---- Exercise 1 ----
employee = {"name": "Joshua", "age": 21, "role": "Backend"}

# 1.
print(employee)
print(len(employee))

# 2.
print(employee["name"])

# 3.
employee["salary"] = 25000
print(employee)

# 4.
employee["role"] = "Fullstack"
print(employee)

# ---- Exercise 2 ----
employee = {"name": "Joshua", "age": 21, "role": "Backend", "salary": 25000}

# 1.
print(employee.get("email"))

# 2.
print(employee.get("email", "Not provided"))

# 3.
print(employee.keys())
print(employee.values())
print(employee.items())

# 4.
print("role" in employee)

# ---- Exercise 3 ----
employees = {
    "E001": {"name": "Joshua", "role": "Backend", "salary": 25000},
    "E002": {"name": "Maria", "role": "Frontend", "salary": 27000}
}

# 1.
print(employees["E001"]["role"])

# 2.
employees["E003"] = {"name": "Luffy", "role": "Data Engineer", "salary": 30000}
print(employees)

# 3.
employees["E002"].update({"salary": 30000})
print(employees)

# 4.

pop = employees.pop("E001")
print(pop)

print(employees)




