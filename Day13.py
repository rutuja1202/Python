# Sets=>A set is a collection of unique , unordered items.
'''
1. Unoreder items
2. No duplicate items
3. Mutable
4. Heterogeneous items=> different data types
'''
# syntax - fruits={"apple","banana","cherry"}
# print(fruits)

# why sets?
# to store unique values
# used to perform mathmatical opretions like union,intersection,difference
# stored in{1,2,34,"abc",True}
# Automatically remove duplicate items

students={"sajiri","rani","sneha","ranu","sneha"}
print(students)
print(type(students))

# empty set
empty_set=set()
print(type(empty_set)) 

# no duplicate items => remove duplicate items
numbers={1,2,3,4,2,5,7,6,4,8,9,1,3}
print(numbers)

# acess via looping
no={1,20,40,60,100,10,80}
for x in no:
    print(x)

# membership operator => check exit or not using membership operator
print(60 in no)
print(500 in no)
print(500 not in no)
print(10 not in no)

# Add items to a set => add()
# for adding single item
no.add(90)
print(no)
# update() => for adding multiple items
no.update([100,110,120])
print(no)

# remove() => to remove specific item
no.remove(20)
print(no)

# discard() => to remove specific item
no.discard(10)
print(no)
# difference between remove() and discard()
# remove() => if present otherwise it will throw an error
# no.remove(500) # KeyError: 500  
# discard() => if present otherwise it will not throw an error
# no.discard(500) # no error

# pop() => remove random elements
no.pop()
no.pop()
no.pop()
print(no)

# clear() => to remove all items from set
no.clear()
print(no)

# set operations
# union() => merge both sets with unique values
a={1,2,3,4,5,6}
b={4,5,6,7,8}
print(a&b)

# intersection() => common elements from both sets
print(a.intersection(b))

# difference() => elements present in first set but not in second set
print(a.difference(b))
print(b.difference(a))

# symmetric_difference() => elements present in both sets except common elements
# print(a.symmetric_difference(b))
print(a ^ b)

# set functions
# len() => to get number of elements in set
print(len(a))
# min() => to get minimum element from set
print(min(a))
# max() => to get maximum element from set
print(max(a))
# sum() => to get sum of all elements from set
print(sum(a))
# sorted() => to get sorted elements from set
print(sorted(a))

# copyig a set
set_1={10,30,40,60}
set_2={100,300,400,500}

# return a shallow copy of set.
set3=set_1.copy()
set3.add(70)
print(set3)

# frozen set => immutable set
set4=frozenset({"html","css","js"})
print(set4)
# set4.add("react")     # AttributeError: 'frozenset' object has no attribute 'add'


