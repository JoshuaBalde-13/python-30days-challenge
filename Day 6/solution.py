# Day 06 - Sets
# Write your solutions below.

# ---- Exercise 1 ----

# 1.
skills_joshua = {"Python", "SQL", "Excel", "Git"}
print(skills_joshua)
print(len(skills_joshua))

# 2.
skills_joshua.add("Power BI")
print(skills_joshua)

# 3.
skills_joshua.discard("Excel")
print(skills_joshua)

# 4.
print("SQL" in skills_joshua)

# ---- Exercise 2 ----
skills_joshua = {"Python", "SQL", "Excel", "Git"}
skills_maria = {"SQL", "Excel", "Figma", "HTML"}

# 1.
both_skills = skills_joshua & skills_maria
print(both_skills)

# 2.
unique_skills = skills_joshua | skills_maria
print(unique_skills)

# 3.
different_skills = skills_joshua - skills_maria
print(different_skills)

# 4.

symmetric_skills = skills_joshua ^ skills_maria
print(symmetric_skills)

# ---- Exercise 3 ----
raw_ages = [24, 31, 28, 31, 24, 45, 19, 31]


# 1.
converted_sets = set(raw_ages)
print(converted_sets)

# 2.
clean_list = list(converted_sets)
clean_list.sort()
print(clean_list)

# 3.
team_a = {"Joshua", "Maria", "Juan"}
team_b = {"Maria", "Ana"}

copy_of_team_a = team_a.copy()

removed_item = copy_of_team_a.pop()

print(f"Existing set: {team_a}")
print(f"Removed item: {removed_item}")