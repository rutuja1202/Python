# Looping Statements in Python
# while loop
# 1
a=1
while(a<=10):
    print("Welcome to python programming",a)
    a+=1

# 2
b=1
while(b<=100):
    print(b,end=" ")
    b+=1  

# 3 check even numbers between 1 to 100
c=1
while(c<=100):
    if c%2==0:
        print(c,end=" ")
    c+=1

# 4 check prime no between 1 to 50
d=1
while(d<=50):   
    count=0
    e=1
    while(e<=d):
        if d%e==0:
            count+=1
        e+=1
    if count==2:
        print(d,end=" ")
    d+=1

print("****************************************************")
 
# do while loop 
# Python does not have a built-in do-while loop construct like some other programming languages. However, you can simulate a do-while loop using a while loop with a break statement. Here's an example:

a=1
while True:
    print("Hello Welcome to do While Loop")
    a+=1
    if a>5:
        break

print("****************************************************")
# for loop
# 1
for i in range(1,11):
    print(i)

# 2
for j in range(1,101):
    print(j)

# 3 even numbers between 1 to 100
for k in range(1,101):
    if k%2==0:
        print(k)
    
# 4
for i in range(1,100,2):
    print(i)

print("****************************************************")
# for else
for i in range(2,10):
    print(i)
else:
    print("Loop is completed")

print("****************************************************")
# break continue 
# 1
for a in range(1,10):
    print(a)
    if a==5:
        break

# 2
for b in range(1,10):
    print(b)
    if b==5:
        continue

print("****************************************************")
# nested loop
for i in range(2,5):
    for j in range(3,6):
        print(i,j)
    