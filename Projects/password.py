import random
def func01():
    while True:
        lengthofpass = int(input("Enter the length of the passwrod you want generate: "))

        if lengthofpass <= 0:
           print("Please Enter valid length")
           continue
        UpperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        Numbers = "1234567890"
        letters = "abcdefghijklmnopqrstuvwxyz"
        characters = "!@#$%^&*()_+-=[]{}|;:,.<>?/"

        addition = UpperCase + Numbers + letters + characters

        password = "".join(random.choice(addition) for _ in range(lengthofpass))

        print(f"Generated password: {password}")
        
        break
func01()