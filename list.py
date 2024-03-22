
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


Getting the size of Python list

# Creating a List
List1 = []
print(len(List1))

                                  Taking Input of a Python List
                                  
                                  
# Python program to take space
# separated input as a string
# split and store it to a list
# and print the string list

# input the list as string
string = input("Enter elements (Space-Separated): ")

# split the strings and store it to a list
lst = string.split() 
print('The list is:', lst) # printing the list

strip function
Remove spaces at the beginning and at the end of the string:



append 
just add the value at end of the list
List = []
print("Initial blank List: ")
print(List)
 
# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

insert 

if you using insert we need mention postion and value 
like below
Syntax. list.insert(pos, elmnt)


List = [1,2,3,4]
print(List)

List.insert(3,5)
List.insert(0,'sreenath')
print(List)
output
[1, 2, 3, 4]
['sreenath', 1, 2, 3, 5, 4]

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


 -------------------------------------------Reversing a list----------------------------------------------------------
mylist = [1, 2, 3, 4, 5, 'Geek', 'Python']
mylist.reverse()
print(mylist)

['Python','Geek',5,4,3,2,1]

----------------------------------------------------------------------------------------------------------------
words=['abc','xyz','aba','1221']

Write a Python program to count the number of strings from a given list of strings. The string length is 2 or more and the first and last characters are the same.



words=['abc','xyz','aba','1221','ujjawalau']
def match_words(words):
       ctr=0
       for word in words:
           if len(word) >1 and word[0]==word[-1]:
               ctr +=1
       return ctr


print(match_words((words)))

ouput
3
