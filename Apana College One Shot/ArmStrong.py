# finding armstrong for any number

n=int(input("Enter the number  "))
temp=n
sum=1
ex=n
p=0
count=0
s=0

while n>0:        # it is used yo find digit in number
    dig=n%10
    n=n//10
    count+=1

while(ex>0):
    p=count
    sum=1
    dig=ex%10
    while p>=1:
        sum=sum*dig
        p-=1
    
    s=s+sum              # Add cube of each number 
    ex=ex//10
    
if s==temp:
    print("Armstrong")
else:
    print("not Armstrong")
    