# Checkpoint - Days 1-7 Combined Project
# Write your solutions below.

# ---- Part 1 ----
full_name = " Bryan Joshua Balde  "
age = 20
salary = 100000
is_active = True


clean_name = full_name.strip().split()[0]
print(clean_name)

summary = (f"My name is {full_name.strip()} and i'm {age} and my salary goal to achieve is {salary}")
print(summary)

bonus_ = 0.10

bonus_ammount = salary * bonus_
total_pay = (salary + bonus_ammount)
print(total_pay)


# ---- Part 2 ----

employee = {"name": full_name.strip(), "age": age, "salary": salary, "active": is_active }
print(employee)

employee_info = ("E001", "12-13-2028", "01-13-2006")
employee_id, hire_date, birth_date = employee_info

skills_list = ["Python", "SQL", "Power BI", "Excel"]

employee["employee_id"] = employee_id
employee["skills"] = skills_list

print(employee)

# ---- Part 3 ----
full_name2 = "Monkey D Luffy"
age2 = 19
salary2 = 30000
is_active = True

skills_list2 = ["Snowflake", "SQL", "Java", "C#"]

employee2 = {"name": full_name2, "age": age2, "salary": salary2, "skills": skills_list2}

print(employee2)

converted_set1 = set(skills_list)
converted_set2 = set(skills_list2)

print(converted_set1 & converted_set2)
print(converted_set1 - converted_set2)


# ---- Part 4 ----

print(employee2.get("bonus", "No Bonus"))

raw_salaries = ["25000", "27000", "25000", "31000", "27000"]
raw_salary1= float(raw_salaries[0])
raw_salary2= float(raw_salaries[1])
raw_salary3= float(raw_salaries[2])
raw_salary4= float(raw_salaries[3])
raw_salary5= float(raw_salaries[-1])

clean_list = {raw_salary1, raw_salary2, raw_salary3, raw_salary4, raw_salary5}
print(clean_list)


# ---- Part 5 ----

print(f"""
Summary:
{employee}
Name: {employee['name']}
Age: {employee['age']}
Salary: {employee['salary']}
Total Pay: {total_pay}
Skills: {employee['skills']}
Employee ID: {employee['employee_id']}
""")
