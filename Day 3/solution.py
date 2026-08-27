# Exercise 1

full_name = "  Bryan Joshua Balde  "
# 1.
print(full_name.strip())

# 2.
print(full_name.upper())
print(full_name.lower())

# 3.
strip_ver = full_name.strip()
print (len(strip_ver))

# 4.
print(strip_ver[0], strip_ver[-1])

# Exercise 2
email = "joshua.balde@gmail.com"

# 1.
at_index = email.find("@")
print(email[0:at_index])

# 2.
print(email)
print(email.split("@"))

# 3.
replace_ver = (email.replace("gmail.com", "outlook.com"))
print(replace_ver)

# 4.
print(strip_ver.count("a"))

# Exercise 3
skills = "Python-SQL-Excel"

# 1.
split = skills.split("-")
print(split)

join = ", ".join(split)
print(join)

# 2.
print(f"Name: {strip_ver} \nEmail: {email} \nSkills: {join}")

# 3.

print(f"Name:\t{strip_ver}")
print(f"Email:\t{replace_ver}")
print(f"Skills:\t{join}")




