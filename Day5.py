# Control Statments
# Conditinal Statments(Decision Making) in Python

# if if else statments - used to excute a block of code based on a condition
# chweck if a number is even or odd
# if
num=int(input("Enter a Number:"))
if(num%2==0):
    print(f"{num} is Even Number")
if(num%2!=0):
    print(f"{num} is Odd Number")

# if else
age=int(input("Enter your age:"))
if(age>=18):
    print("Welcome...")
else:
    print("Sorry...")


num=int(input("Enter a Number:"))
if(num%2==0):
    print(f"{num} is Even Number")
else:
    print(f"{num} is Odd Number")

# if elif else
# 
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if(a>=b):
    print(f"{a} is greatest number")
elif(b>=c):
    print(f"{b} is greatest number")    
else:
    print(f"{c} is greatest number")
        
print('**************************************')

# Match Case statments (Python 3.10 + version)
# similar to switch case in other programming languages

order=input("what would you like to eat :")
match order:
    case "pizza":
        print("Available ")
    case "burger":
        print("Available ")
    case "pasta":
        print("Not Available ")
    case "steam veg momos":
        print("Available ")
    case "maggie":
        print(" Available ") 
    case _:
        print("Please choose from the menu")