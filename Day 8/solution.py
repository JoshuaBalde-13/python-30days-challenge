# Day 08 - Conditionals
# Write your solutions below.

# ---- Exercise 1 ----
employee = {"name": "Joshua", "age": 21, "salary": 39999}

if employee["age"] >= 18:
    print("Adult")
else:
    print("Minor")


if employee["salary"] < 20000:
    print("Low Income")
elif employee["salary"] < 40000:
    print("Mid Income")
else:
    print("High Income")


if 'email' not in employee:
    print("Missing email")
else:
    print("Has email")


# ---- Exercise 2 ----
employee = {"name": "Maria", "age": 25, "years_of_service": 4, "performance_score": 8.2}

if employee["performance_score"] >= 7 and employee["years_of_service"] >= 2:
    print("Eligible for raise")
else:
    print("Not eligible yet")

if employee["age"] >= 18:
    if employee["years_of_service"] >= 3:
        print("Senior adult employee")
    else:
        print("Junior adult employee")
else:
    print("Underage — invalid record")


if employee["performance_score"] < 5 or employee['years_of_service'] < 1:
    print("Needs Review")
else:
    print("No Review Needed")

# ---- Exercise 3 ----

bio = ""
skills = []

if bio:
    print("Has bio")
else:
    print("Missing Bio")

if skills:
    print(f"Skill listed {skills}")
else:
    print("No skill listed")

# in truthy and falsy python treats the 0, Empty, or None it's automatically false while the variable has a value it's automatically true

salary = 0

if salary:
    print(f"Your salary {salary}")
else:
    print("No Salary")


one_line = "Adult" if employee["age"] >= 18 else "Minor"
print(one_line)

