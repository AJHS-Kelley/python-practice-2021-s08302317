# Grade calculator practice, 11/16/21

print("this program will take a numerical grade between 0 and 100 and print the letter grade.\n")
grade = float(input("please enter the numerical grade including the decimal"))
print(grade)

if grade >= 89.5:
    print("That grade is a A.\n")
elif grade >= 79.5:
    print("That grade is a B.\n")
elif grade >= 69.5:
    print("That grade is a C.\n")
elif grade >= 59.5:
    print("That grade is a D.\n")
else:
    print("That grade is a F.\n")
    