tuple in python

Python Tuple is a collection of objects separated by commas. In some ways, a tuple is similar to a Python list in terms of indexing, nested objects, and repetition but the main difference between both is Python tuple is immutable, unlike the Python list which is mutable.



Creating Python Tuples
There are various ways by which you can create a tuple in Python. They are as follows:

Using round brackets
With one item
Tuple Constructor
Create Tuples using Round Brackets ()
To create a tuple we will use () operators.
example
var = ("Sreenath", "and", "Ujjwala","best","friends")

output:-('Sreenath', 'and', 'Ujjwala', 'best', 'friends')

#one more way we can create tuple in python from Python 3.11
#values : tuple[int | str, ...] = (1,2,4,"Geek")

#print(values)


print(var)


What is Immutable in Tuples?
---------------------------------------------------------------------------------------------------
Tuples in Python are similar to Python lists but not entirely. Tuples are immutable and ordered and allow duplicate values. Some Characteristics of Tuples in Python.

We can find items in a tuple since finding any item does not make changes in the tuple.
One cannot add items to a tuple once it is created. 
Tuples cannot be appended or extended.
We cannot remove items from a tuple once it is created. 


ytuple = (1, 2, 3, 4, 5)

# tuples are indexed
print(mytuple[1]) #2
print(mytuple[4]) #5



mytuple = (1, 2, 3, 4, 5)


mytuple[1] = 100
print(mytuple)

error:

 mytuple[1] = 100
    ~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment  





Below are the different operations related to tuples in Python:

Concatenation
Nesting
Repetition
Slicing
Deleting
Finding the length
Multiple Data Types with tuples
Conversion of lists to tuples
Tuples in a Loop


# Code for concatenating 2 tuples
example:1
tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'programming')

print(tuple1+tuple2)


output
(0, 1, 2, 3, 'python', 'programming')
example:2
tuple1 = (0,1,2,3)
tuple2 = (2,3,5,6)
print(tuple1+tuple2)
output
(0, 1, 2, 3, 2, 3, 5, 6)


nested tuples
tuple3=(tuple1,tuple2) 

output

((0, 1, 2, 3), (2, 3, 5, 6))

print(tuple3[3])

print(tuple3[3])


output
          ~~~~~~^^^
IndexError: tuple index out of range


tuple1 = (0,1,2,3)
tuple2 = (2,3,5,6)

#((0, 1, 2, 3), (2, 3, 5, 6))
tuple3=(tuple1,tuple2)
print(3*tuple3)

output
((0, 1, 2, 3), (2, 3, 5, 6), (0, 1, 2, 3), (2, 3, 5, 6), (0, 1, 2, 3), (2, 3, 5, 6))
we want remove the (1,)
The original list : [(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
Filtered list : [(4, 5), (8, 6, 7), (3, 4, 6, 7)]



tuple1=[(4, 5), (4, ), (8, 6, 7), (1, ), (3, 4, 6, 7)]
k=(1,)
val=[n for n in tuple1 if n!=k]
print(val)


output:-
[(4, 5), (4,), (8, 6, 7), (3, 4, 6, 7)]



tup = (1, 2, 3, 4, 3, 5)
#Remove 3 from given list
tu=3
x=[x for x in tup if x!=tu ]
print(x)
output

[1, 2, 4, 5]


tup = ('H', 'e', 'l', 'l', 'o')
tu="".join(tup)

print(tu)
Join:-all items in a tuple into a string, using a hash character as separator
ouput
Hello
