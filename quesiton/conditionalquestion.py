a1 = int(input("Enter ur 1st number: "))
a2 = int(input("Enter ur 2nd number: "))
a3 = int(input("Enter ur 3rd number: "))
a4 = int(input("Enter ur 4th number: "))

if (a1>a2 and a1>a3 and a1>a4):
    print(f"{a1} is the greatest number")

if (a2>a1 and a2>a3 and a2>a4):
    print(f"{a2} is the greatest number")

if (a3>a1 and a3>a2 and a3>a4):
    print(f"{a3} is the greatest number")

if (a4>a2 and a4>a3 and a4>a1):
    print(f"{a4} is the greatest number")