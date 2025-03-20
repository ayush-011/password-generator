def new_func():
    while True:
        print('''\n// Calculator //\n
        Choose what task you want to perform
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division
        5.Exit\n''')

        choice = int(input("Please choose form 1/5 11to perform specfic task: "))

        if choice == 1:
                a = int(input("Enter the number: "))
                b = int(input("Enter the another number: "))
                print(f"Sum of {a} and {b} is",a+b)
        elif choice == 2:
                a = int(input("Enter the number: "))
                b = int(input("Enter the another number: "))
                print(f"Subtraction of {a} and {b} is",a-b)
        elif choice == 3:
                a = int(input("Enter the number: "))
                b = int(input("Enter the another number: "))
                print(f"Multiplication of {a} and {b} is",a*b)
        elif choice == 4:
                a = int(input("Enter the number: "))
                b = int(input("Enter the another number: "))
                print(f"Division of {a} and {b} is",round(a/b,2))
        elif choice == 5:
                break

        else:
                print("You Entered wrong number,Please choose no. form 1 / 5")

new_func()