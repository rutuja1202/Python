# 1.Write a Python program to take a user’s name and age as input and print:
#    Hello <name>, you are <age> years old!
name=input("Enter your name:")
age=input("Enter your age:")
print(f"My name is {name} and I am years {age} old.")

# Write a program to check whether a number entered by the user is even or odd.
num1=int(input("Enter a number: "))
def num(n):
    if n%2==0:
        print("Even  Number")
    else:
        print("Odd Number")
num(num1)

# Write a program to find the largest of three numbers using if-elif-else.
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Largest number is:", a)
elif b >= a and b >= c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

# Write a program to calculate the sum of numbers from 1 to N using a for loop.
N = int(input("Enter a number (N): "))

total = 0

for i in range(1, N + 1):
    total = total + i

print("Sum of numbers from 1 to", N, "is:", total)

# Write a program to print the multiplication table of a number using a loop.
no=int(input("Enter a number: "))
def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
table(no)

# Write a function greet(name) that prints a greeting message.
def greet(name):
    print("Hello,", name + "! Welcome!")
greet("Rutuja")
