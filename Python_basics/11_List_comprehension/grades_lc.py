# create a list of grades, 
# and then a comprehensive list of passing grades (>= 60)
grades = [85, 42, 79, 90, 56, 61, 30]
passing_grades = [grade for grade in grades if grade >= 60]

print(passing_grades)