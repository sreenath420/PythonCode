
-------------------------------------------------------------------------Python_List-------------------------------------------------------------


Python Lists are just like dynamically sized arrays, declared in other languages (vector in C++ and ArrayList in Java). In simple language, a list is a collection of things, enclosed in [ ] and separated by commas.

example
Var = ["Geeks", "for", "Geeks"]
print(Var)

output

["Geeks", "for", "Geeks"]


Lists are the simplest containers that are an integral part of the Python language. Lists need not be homogeneous always which makes it the most powerful tool in Python. A single list may contain DataTypes like Integers, Strings, as well as Objects. Lists are mutable, and hence, they can be altered even after their creation.


Accessing elements from the List
----------------------------------

n order to access the list items refer to the index number. Use the index operator [ ] to access an item in a list. The index must be an integer. Nested lists are accessed using nested indexing


Accessing elements from a multi-dimensional list
----------------------------------------------------\

nested list having muliptle sublist kind inside the list we can access index value from given sublist value

List = [['Sreenath', 'For'], ['Ujjwala','Learning','Dance']]
print(List[0][1])
print(List[1][0])
output:-
For
Ujjwala

List = [['Sreenath', 'For'], ['Ujjwala','Learning','Dance']]
i want ouput is here learnign how to get accesss here throught nested list
verfiy the below code
print(List[1][1])



Negative indexing
In Python, negative sequence indexes represent positions from the end of the array. Instead of having to compute the offset as in List[len(List)-3], it is enough to just write List[-3]. Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second-last item, etc.


List = [1, 2, 'Sreenath', 4, 'For', 6, 'Ujjwala']

print("Accessing element using negative indexing")
 
# print the last element of list
print(List[-1])
 
# print the third last element of list
print(List[-3])

output

Accessing element using negative indexing
Ujjwala
For


sample program
--------------------------------------------------------
Adding

list=[1, 2, 8]
result=0
for i in list:
    result+=i
print(result)


Mutliple 
-----------------------------------------------------------------

list=[1, 2, 8, 4]
result=1
for i in list:
    result=result*i
print(result)

