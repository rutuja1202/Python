# String => Is a collection or sequence of charater i.e number , charater

#must be stored in =>" " or '' or """ """

name="raju"
print(name)

# String catneation => +

skill="Python"
role="python developer"
print(skill+role)
print(skill,role)

# string repetion
print(skill*3)

# membership opretor =>
result="R" in skill 
print(result)

# immutable
str1="ABC"
str2="XYZ"

str1="raj"
print(str1)
print(str2)

# ***********************************************
# Methods in function
# len() =>
role="python full  Stack developer"
print(role)
print(len(role))  #count including spacing also

# upper()
print(role.upper())
# lower()
print(role.lower())
# capitalize()
print(role.capitalize())
# titile()
print(role.title())
#replace()
str4="react js"
print(str4.replace('react','angular'))
# ************************************************
# find()=>return index of a given chrater from a string
print(str4.find('a'))
# count()=>return the occurence of specific chracter
print(str4.count('a'))
# split()=>it split our given string into list
            # convert string into list
print("a,b,c,d,e,f,g".split(" , "))
# join()=>used to convert list into string
str5=["i","am","here"]
print(str5)
print("".join(str5))
print("*".join(str5))

# **********************************************
# for loop
str6="Python full stack develper"
reversed_str6= " ".join(str6.split()[::-1])
print(reversed_str6)

