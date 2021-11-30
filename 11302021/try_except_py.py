# Try / Except, 11/30/21

y = 25
my_name = "Lorenzo Saliard"

try:
    print(x)
except:
    print("Oh no, something is burning!\n")

try:
    print(z)
except NameError:
    print("That variable is not defined, let's define it. ")
    z = 25
except:
    print("Oh no, something is burning!\n")

print(z)
