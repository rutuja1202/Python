# Default parameters =>
# use to handle arguments when we don't pass sufficient arguments 
# at that time we can handle it by using default values without any error
'''def sum(a,b,c,):
     print(a+b+c)
sum(1,2,3)'''
# sum(10) => TypeError: sum() missing 2 required positional arguments: 'b' and 'c'

# 1
def add(a=0,b=0,c=0):
    print(a+b+c)
add(10,20)
add(10)
add()

# 2
def mult(a,b=1):
    return a*b
result = mult(20)
print(result)

# 3
def emp(name="ram",role="None",skill="python"):
    print(f"your name is {name} , your role is {role} , your skill is {skill}")
emp("Aditi","Python developer","Django")
emp("Aditi","Python developer")
emp("Aditi")

# Python we can pass parameters namealso as per our order while function calling.
emp(role="Python developer",name="Aditi",skill="Django")

# ************************************************************************

# Arguments =>
# used to handle extra / additional arguments which we passed while function calling
# return the value in a tuple laike (...) i.e immutable (cannot be changed)
# 1
'''def add(x=0,y=0,z=0):
    return x+y+z
add(10,20,30,40,50)''' # TypeError: add() takes from 0 to 3 positional arguments but 5 were given

# 2
'''def sum(a=0,b=0,c=0,*args):
    # print(a+b+c)
    # print(args)
    sum=a+b+c
    for i in args:
        print(i)
        sum(i)
    print("sum is" , sum)

sum(10,20,30,40,50,60,70)'''

#*******************************************

# Recursive Function => is a function that calls itself during its excution
# its solve a big problem by breaking it into smaller subproblems
# used for => matematival problems,searching sorting

# base case=>condition  where  recursion stops.prevents infinite calls
# recursive case=>part where the function calls itself with a smaller or simpler input
# Syntax
'''def function_name(parameters):
     if base_condition:
        return some_Value
     else:
         return function_name(smaller_value)'''

# ***********************************************

# 1 Factorial  number

def fact(number):
    if number==0:
        return number  #base case
    else:
        return number*fact(number-1)
result=fact(5)
print(result)

# reverse addition with recursive function
def reverse_num(n):
    if n == 0:
        return 0
    return (n % 10) * (10 ** (len(str(n)) - 1)) + reverse_num(n // 10)


def reverse_add(n):
    return n + reverse_num(n)
num =int(10 9 8 7 6 5 4 3 2 1):
print("Reverse Addition:", reverse_add(num))
