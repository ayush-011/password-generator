def greatest(n1,n2,n3):
    if (n1>n2 and n1>n3):
        print(f"Greatest Number{n1}")
    elif (n2 > n3 and n2 > n1):
        print(f"Greatest NUmber{n2}")
    elif (n3 > n2 and n3 > n1):
        print(f"Greatest Number{n3}")
n1 = int(input())
n2 = int(input())
n3 = int(input())
print(greatest(n1,n2,n3))
print(greatest(n1,n2,n3))
    