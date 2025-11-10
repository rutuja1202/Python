# Opretors in python
# Arithmetic operators
''' +
 -
 *
 /
 %
** '''
a=10
b=3
print(a+b)
print(a-b)
print(a*b)  
print(a/b)
print(a%b)
print(a**b)
# ********************************************
# Floor division
print(a//b)
# ********************************************
x=20
y=10
print(x+y-x*y/x)
# ********************************************
# Comparison operators
'''
==
!=
>
<
>=
<=
'''
a=100
b=200
print(a==b)
print(a!=b)
print(a>b)
print(a<b)
print(a>=b)
print(a<=b)
# ********************************************

# Logical operators
# use to check conditions
''' 
and
or
not
'''
# And operator => All conditions should be true
p=10
q=30
r=50
print(p>q and q<r)  # False and True => False
print(q>p and q>r)  # true and false => false

# or operator => At least one condition should be true
print(q>p or q>r)  # true or false => true
print(p>q or q<r)  # false or true => true

# not operator => Reverse the result
# when condition is true => not true => false
# when condition is false => not false => true
print(not(p>q))  # not false => true

# ********************************************
# Assignment operators
'''
=
+=
-=
*=
/=
%=
**=
'''
name="ram"
print(name)

a=20
b=a
print(a)
print(b)

age=30
age+=5
age-=2
age*=2
age/=2
age%=2
age**=2 
print(age)
print('******************************************')
# ********************************************
# Bitwise operators
''' 
&
|
^
~
<<
>>
'''
print(20 & 30)  # 20
print(12 & 6)   # 4
print(2 & 3)    # 2
print(20 | 30)  # 30
print(12 | 6)   # 14    
print(2 | 3)    # 3
print(20 ^ 30)  # 10
print(12 ^ 6)   # 10
print(2 ^ 3)    # 1
print(~2)       # -3
print(~3)       # -4
print(5 << 2)   # 20
print(10 << 3)  # 80
print(20 >> 2)  # 5
print(40 >> 3)  # 5
print('******************************************')
# ********************************************
# Ternary operator
# check the condition and assign value based on condition
# lie if else conditions in single line
# syntax => value1 if condition else value2

age=int(input("Enter your age:"))
result="Your are eligible to vote" if age>=18 else "Your are not eligible to vote"
print(result)

