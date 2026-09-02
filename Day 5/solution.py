# Day 05 - Tuples
# Write your solutions below.
employee_record = ("Joshua", 21, "Backend")

# ---- Exercise 1 ----
# 1.
print(employee_record)
print(len(employee_record))

# 2.
print(employee_record[0], employee_record[-1])

# 3. 'tuple' object does not support item assignment



# ---- Exercise 2 ----
coordinates = (14.5995, 120.9842, "Manila")

# 1.
latitude, longitude, city = coordinates
print(latitude)
print(longitude)
print(city)

# 2.
scores = (8, 9, 7, 9, 10, 9)
print(scores.count(9))

# 3.
print(scores.index(10))

# 4.
print(7 in scores)

# ---- Exercise 3 ----

# 1.
skills = "Python", "SQL", "Excel"
print(type(skills))

# 2.
converted_tuple = list(skills)
converted_tuple.append("Power BI")

print(converted_tuple)

skills = tuple(converted_tuple)
print(skills)

# 3. 
employees = (
    ("Joshua", 21, "Backend"),
    ("Maria", 26, "Frontend"),
    ("Juan", 30, "Database")
)
print(employees[2][2])

# 4. I will use tuple for a fixed value like a birthday, student id number