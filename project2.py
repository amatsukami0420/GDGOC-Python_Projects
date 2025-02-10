# Project 2 by FA24-BCS-110
a=int(input("Enter The First Number: "))
operator=input("Enter the operator (+, -, *, /): ")
b=int(input("Enter The Second Number: "))
if operator=="+":
    print("The Answer is: ", a+b)
elif operator=="-":
    print("The Answer is: ", a-b)
elif operator=="*":
    print("The Answer is: ", a*b)
elif operator=="/":
    if b!=0:
        print("The Answer is: ", a/b)
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid input.")