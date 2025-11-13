# Functions in a pyhton
# def keyword to use to define a function 
# write once and resused multipe times
# is a block of code i,e is a bunch of statments
# synatx
'''
//function declaration
def function_name(parameters):
    block of code

//function call
function_name(arguments)
'''
# 1
'''def demo():
    print("Hello World")
demo()  # function call'''

# 2
def function1():
    for i in range(1,101):
        print("Hello World", i)
function1()

# 3
def sum():
    print(100+20)
sum()

# Function with Parameters and Arguments
# parameters and arguments are used to make dynamic function
# function take input and return output as a result
# parameters-such a values/variable which we are passing while function declaration
# arguments-Actual values which we are passing while function calling which are referred as arguments 

def add(a,b):
    print(a+b)
add(10,20)
add(100,200)
add(5,15)

# **************************************************
def user(name,skill,age):
    print(f""" 
your Name is {name}
your Skill is {skill}
your Age is {age}
""")
user("ram","python",50)

# **************************************************
# even odd function
num1=int(input("Enter a number: "))
def num(n):
    if n%2==0:
        print("Even  Number")
    else:
        print("Odd Number")
num(num1)
# num(7)
# num(0)
# num(12345678936789)
# **************************************************

# Return Keyword in Function
# used to retrun a value outside the function back
# it stops the excution after return statement

# 1
def add2(x,y,z):
    return (x+y+z)
result=add2(10,20,30)
print(result)

# 2
def square(no):
    return no**2
print(square(5))

# 3
def demo(msg):
    print("Hello A")
    return msg      
print("World B")  
result3=demo("Good Afternoon ")
print(result3)

