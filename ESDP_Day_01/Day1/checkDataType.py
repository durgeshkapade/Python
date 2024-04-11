a=5
b = 3.12
c = True
d = "Durgesh"
print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))

# using id we check address of variable
print(id(a))

# preform Arithmatic operation
a = 10
b = 20
'''
print("Addition of       ",a," and ",b," is ",a+b)
print("Substraction of   ",a," and ",b," is ",a-b)
print("Multiplication of ",a," and ",b," is ",a*b)
print("Division of       ",a," and ",b," is ",a/b)'''

# assignment operator
result = a%b
# print(result)

# type Casting 

# p=int(input("Enter the value"))
# print(p)
print(float("5"))
print(complex(5))
print(complex(True))
# print(complex("name"))   # give error
print(bool(45))
print(bool(4.5))
print(bool(-1))
print(bool(1+4j))
# print(bool(1+4j))

# same address if value is same
math = 1
sci = 1
print(id(math))
print(id(sci))


