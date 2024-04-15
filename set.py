---------------------------------------------------------------Set-----------------------------------------------------
A Set in Python programming is an unordered collection data type that is iterable, mutable and has no duplicate elements. 

Set are represented by { } (values enclosed in curly braces)



The major advantage of using a set, as opposed to a list, is that it has a highly optimized method for checking whether a specific element is contained in the set. This is based on a data structure known as a hash table. Since sets are unordered, we cannot access items using indexes as we do in lists.


example

var = {"Python", "for", "Python"}
print(var )
set is removing duplicates
o/P

{'for', 'Python'}
# typecasting list to set
we can create set by using list creation and mentions type set if we don't mention there set its going to list only
myset = set(["a", "b", "c"])
print(type(myset))


myset = set(["a", "b", "c"])


# Adding element to the set
myset.add("d")
print(myset)

here elements are printing unordered because of set follows unordered way
o/p 
{'d', 'a', 'b', 'c'}


myset = {"Python", "for", "Python"}
print(myset)

# values of a set cannot be changed
myset[1]="Hello"
print(myset)

error:
  myset[1]="Hello"
    ~~~~~^^^
TypeError: 'set' object does not support item assignment

#remove the elements
myset = {"Python", "for", "Python"}

myset.remove('for')

print(myset)

o/p:-

{'Python'}



---------------------------------->Python Frozen Sets<-------------------------------------------
Frozen sets in Python are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied. It can be done with frozenset() method in Python.

While elements of a set can be modified at any time, elements of the frozen set remain the same after creation. 

If no parameters are passed, it returns an empty frozenset.

frozen_set = frozenset(["e", "f", "g","g"])

print("\nFrozen Set")
print(frozen_set)



{'a','b','c','d','e'}
 0   1    2   3   4
 
 0 --> a b
 
 
 
  

Methods for Sets


Adding elements to Python Sets

insertion in the set is done through the set.add() function, where an appropriate record value is created to store in the hash table.


people = {"Sreenath", "Ujjawala", "Archi"}

#print("People:", end=" ")
#print(people)
people.add("Sree")
#print(people)

for i in range(1,6):
    people.add(i)
print(people)

o/parameters
{1, 2, 3, 4, 5, 'Ujjawala', 'Sree', 'Sreenath', 'Archi'}



------>union<------
by using union we can add multiple sets in python

like below example

people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}

union_put=people.union(vampires)
print((union_put))
union_all=people.union(vampires).union(dracula)
print((union_all))

o/p

{'Idrish', 'Karan', 'Archil', 'Jay', 'Arjun'}
{'Idrish', 'Karan', 'Raju', 'Deepanshu', 'Archil', 'Jay', 'Arjun'}

is_subset
people = {"Jay", "Idrish", "Archil"}
vampires = {"Idrish", "Archil"}
dracula = {"Deepanshu", "Raju"}

union_put=people.issubset(vampires)
print((union_put))

union_put1=vampires.issubset(people)

print((union_put1))


o/p

False
True

intersection
common values between two sets
people = {"Jay", "Idrish", "Archil","Sreenath","Ujjwala"}
vampires = {"Sreenath", "Ujjwala"}


o/p

{'Ujjwala', 'Sreenath'}


difference
uncommon elements between both sets


people = {"Jay", "Idrish", "Archil","Sreenath","Ujjwala"}
vampires = {"Sreenath", "Ujjwala"}
dracula = {"Deepanshu", "Raju"}

union_put=people.difference(vampires)

o/p:-
{'Archil', 'Jay', 'Idrish'}




differnece 



Example coding

list1 = {1, 2, 3, 4, 5, 6}

list2 = {4, 5, 6, 7, 8}

set1=list2-list1
set2=list2.difference(list1)
print(set1)
print(set2)
o/p
{8, 7}
{8, 7}



ar1 = {1, 5, 10, 20, 40, 80}
ar2 = {6, 7, 20, 80, 100}
ar3 = {3, 4, 15, 20, 30, 70, 80}
#Output :-[80,20]
set1=ar1.intersection(ar2).intersection(ar3)
print(set1)
o/p
{80, 20}
