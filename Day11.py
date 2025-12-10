
# tuples-

# Is a collection of similar or different type of element
# we can stored multiple types of data in a single variable
# Immutable i.e we can't update / change

# Fixed size length stored in memory like a pointer

# syntax - ()

# starts indexing from 0


tuple_1=(10,20,30,60,80,100,"ABC",True,None)

print(tuple_1)
print(type(tuple_1)) # tuple

# We can stored tuple without ()

tuple_2=10,1000,500,700,1000
print(tuple_2)
print(type(tuple_2))


# single tuple element must have ,

# tuple_3=("Pratik") # str
tuple_3=("Pratik" ,) # tuple
print(tuple_3)
print(type(tuple_3))

# ******************************************************************8


# accessing tuple

tuple_4=("ABC","XYZ","PQR")

print(tuple_4[1])
print(tuple_4[-1])



# ************************************************************************

# iterating

for x in tuple_4:
    print(x)



# 🔹 Tuples Are Immutable

skill=("HTML","JS","React","Python","AWS","LLM","NLP","ML")
# skill[2]="Next JS"

print(skill)


# ***********************************************************
# tuple slicing
# exract piece of data from tuple
# it will ignore last index element
# [start:end]

print(skill[2:6])

# i wanna last element
print(skill[0:len(skill)])

print(skill[4]) # AWS

print(skill[4:])


print(skill[:4])



# 🔍 Searching in a Tuple
# in
# not in


result1="AWS" in skill
print(result1) # True


result1="AWS" not in skill
print(result1) # False


# ************************************
# count() - count the occurence of specific element inside tuple
tuple_5=(50,40,60,80,100,40,20,40,20,30,10,60,20)
print(tuple_5.count(20))

print(tuple_5)



# index()
# return index of specific element
print(tuple_5.index(20))


# built in function

# min()
# max()
# len()
# sum()



# ******************************************************************


# packing and unpacking


# packing
data=("Pratik","Sumit","Rohan","Mandar","Chaitanya")

print(data)
print(data[0])
print(data[1])
print(data[2])



# unpacking
name1,name2,name3,name4,name5=data

print(name1)
print(name4)


# **************************************************

# convert tuple into list
# list

tuple_6=("A","B","C","X","Y")
print(tuple_6)
print(type(tuple_6))


# convert to list
res3=list(tuple_6)
print(res3)
print(type(res3))




# convert list into tuple


list=[100.40,500,"ABC", None, True]
print(list)
print(type(list))

# convert to tuple
a=tuple(list)
print(a)
print(type(a))



res4=(4,5,6)+("ABC",4)
print(res4)



