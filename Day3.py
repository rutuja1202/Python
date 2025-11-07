#Type casting
a=5
b=5
c=10

# convert 1 type to another type


# a = 5
# b = 2.5
# c = "10"
print(a+b+int(c))

# ********************************************

# String concatenation 
name="Rutuja"
skill="PYTHON"
age=21
isEligible=True
print("my name is "+name+" and my skill is "+skill+" and my age is "+str(age)+" i am eligible:"+str(isEligible))
# *********************************************
a=20
b=30
c="40"
print(a,b,c)

# *********************************************
emp="rutuja"
empId="12345"
# print(a+b)
print(emp,empId)
# *********************************************
name1="Rutuja"
name2="Sakshi"
print(name1 + name2)
print(name1,name2)
# *********************************************
x=10
y="ram"
# print(x+y) # TypeError
# print(x,y) =>its convert string into number 
# *********************************************
# f-string 

print(f"my name is {name1} and my friend name is {name2}")

# *********************************************
# Take input from user 
name=input("Enter your name:")
city=input("Enter your city:")
age=input("Enter your age:")
print(f"My name is {name} and my age is {age} and I live in {city}")
# *********************************************
# Keywords in python
import keyword
print(keyword.kwlist)