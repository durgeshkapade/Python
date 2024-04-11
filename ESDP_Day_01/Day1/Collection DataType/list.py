mylist=["Durgesh",3,45.5,"sachin",True]
# accessing by index
# print(mylist[1])
# print(mylist[2])
# print(mylist)

# change value of list
mylist[2]="ram"
# print(mylist)

# add value in list
mylist.append('harsh')
mylist.append('komal')
# print(mylist)

# insert function
mylist.insert(2,True)
# print(mylist)

# remove element 
mylist.remove(True)

#copy list 
list1=mylist.copy()
# print(list1)

l1=["prashant","jha",123]
print(l1*2)
l2=[50,45.3]
print(l1+l2)

#Delete list
l=[2,5,7,89,1]
# del l
# print(l)

# Clear the List
l.clear()
# print(l)

#typecasting
name="Durgesh"
my=list(name)
print(my)  #['D', 'u', 'r', 'g', 'e', 's', 'h']

# Reverse() method
m=[10,20,30,40]
m.reverse()
print(m)




##### Sorting list (Same type of data required)
r=[3,45,7,23,9]
r.sort()
print(r)

######## List in List (multidimensional list)
list=[['prashant',5],[23.5,"dur"],[2341,True]]
# print(list)
# print(list[0][0]) # prashant
# print(list[2][1]) # True


##### Alising
# alising means assinging one variable reference to another
flist=[1,2,3,4]
slist=flist
print(id(flist))
print(id(slist))

