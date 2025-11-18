

# lists

# is a collection of similar of different type of elements
# we can stored mulitple type of data in a single variable i.e int, float, bool,string,none,list,dict

# starts indexing from 0 
# must defined with []

# we can add / update / change anytime i.e mutable

# syntax

# eg . list=["ABC",100,200,True,None,10.20,["A","B","C"]]

list_1=["ABC",100,200,True,None,10.20,["A","B","C"]]
print(list_1)


# list data access - Number indexing

print(list_1[0])
print(list_1[5])
print(list_1[6])
# print(list_1[8])



# we can pass -ve index also  - starts from end

print(list_1[-1]) # ["A","B","C"]
print(list_1[-3]) # None


# ***************************************************************

# We can update lists elements

skills=["HTML","CSS","JS","Python",["Sumit","Harsh","Ajit","Rohan"]]
print(skills)

skills[2]="React JS"
print(skills)
print(skills[2])

print(skills[4])

# harsh
print(skills[4][1])


# *********************************************************

# looping or Iterating list

fruits = ["apple", "banana", "cherry"]
for i  in fruits:
    print(i)


# To perform operations on a list

# add / remove from list

# append()
# pop()

# insert(index,value)

# extends()




# append- used to add elements in the end / last index
        #  original list modified


users=["John","Andrew","Peter","Michael"]
res1=users.append("Mandar")
print(res1)
print(users)


# ******************************************************************


# pop- used to remove element from a last index  and return it 
# pop()- if empt it will remove last element
# pop(index)- now it will remove index element

no=[10,20,50,70,80,100]
print(no)

res=no.pop()
print(res) # 100

print(no)


# *****************************************************

# insert(index,value)
# used to add element at specific position

list_1=["ABC","XYZ","PQR"]

# aman
# list_1.insert(1,"AMan")
list_1.insert(1,["AMAN","JOHN"])

print(list_1)


# ************************************************


# extend

#  add elements from another list i.e merging 2 or more lists

list_2=["Laptop","Mobile","Charger"]
list_3=["HP","APple","Samsung"]

list_3.extend(list_2)
print(list_3)



# **************************************************************

# remove- Used to remove first matching element from given list
# remove(value)

list_4=[100,200,300,600,200]
list_4.remove(200)
print(list_4)


# *****************************************

# clear- empty the list

list_4.clear()
print(list_4)

# ************************************************


# searching in Lists i.e check elements is present or not


fruits = ["apple", "banana", "mango", "grapes"]

# in
# not in

result3="apple" in fruits
print(result3)


result4="apple" not in fruits
print(result4)



# *****************************************************

# sort

# Used to sort list elements in a ascending or descending order
# no=[100,400,50,600,80,100,130,40]

char=['X',"A","Y","B","C","Z","P","D"]
char.sort()
print(char)



# ********************************************


# reverse
# used to reverse given list


fruits = ["apple", "banana", "mango", "grapes"]
fruits.reverse()
print(fruits)

# ***********************************************************************

# Built in Functions

# len()
# min()
# max()
# sum()

list_5=[100,400,50,60,900,1000,150,250,350]
print(len(list_5))
print(sum(list_5))
print(min(list_5))
print(max(list_5))



# ******************************************


# List Slicing
# extract specfic portion from a given list
# [start:end]
print(list_5[1:6])


# ******************************************

# copy method

list6 = [1, 2, 3]
list7=list6
# Avoid using = because it links the same reference.

# copy()

print(list6)
print(list7)

print(id(list6))
print(id(list7))


# ******************************************************

list6 = [1, 2, 3]
# Avoid using = because it links the same reference.

# copy()
list7=list6.copy()

list7.append(100)

print(list6)
print(list7)

print(id(list6))
print(id(list7))








