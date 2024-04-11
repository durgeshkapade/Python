
first=input("Enter the first number  ")
Operator=input("Enter the Operator {+,-,*,/,%}  ")
second=input("Enter the second number     ")

first=int(first)
second=int(second)

if Operator =='+':
    print(first+second)
elif Operator =='-':
    print(first-second)
elif Operator =='*':
    print(first*second)
elif Operator =='/':
    print(first/second)
elif Operator =='%':
    print(first%second)
else:
    print("Enter valid input")
    