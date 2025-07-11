#type casting: the process of converting a variable from one data type to another:
# - str()
# - int()
# - float()
# - bool()

name = "Fra"
age = 25
gpa = 3.2
is_student = True

#to check the type of a variable, we use the functino type(var_name):
print(type(is_student))
#the output is going to be a class, in this case: <class 'bool'>

#to convert from one data type to another:
gpa = int(gpa)
print(gpa)
#int() truncates the decimal part, in this case is going to output 3

print(type(age))
age = str(age)
print(type(age))