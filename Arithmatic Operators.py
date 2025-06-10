a= int(input("Enter a value").strip())
b= int(input("Enter b value").strip())

Max_value=10**10

if 1<= a <=Max_value and 1<= b <=Max_value:
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
else:
    print("Invalid Range")