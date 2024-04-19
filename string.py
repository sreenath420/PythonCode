------------------------------------------------------------------->STRING<----------------------------------------------------------------------------------------------------

A String is a data structure in Python Programming that represents a sequence of characters. It is an immutable data type, meaning that once you have created a string, you cannot change it. Python String are used widely in many different applications, such as storing and manipulating text data, representing names, addresses, and other types of data that can be represented as text.




string_variable = 'Hello, world!'



string_0 = "A Computer Science portal for geeks"
print(string_0)
print(type(string_0))


string='sreenath and ujjwala best friends'

print(string[::0])

print(string[1:5:0])
Note:if you apply slice is step with zero it throws error in python
          ~~~~~~^^^^^
ValueError: slice step cannot be zero

print(string[5:9:2])



string='python'

print(string[1:-2])

output:
yth


Deleting/Updating from a String

n Python, the Updation or deletion of characters from a String is not allowed. This will cause an error because item assignment or item deletion from a String is not supported. Although deletion of the entire String is possible with the use of a built-in del keyword. This is because Strings are immutable, hence elements of a String cannot be changed once assigned. Only new strings can be reassigned to the same name. 


Updating a character
A character of a string can be updated in Python by first converting the string into a Python List and then updating the element in the list. As lists are mutable in nature, we can update the character and then convert the list back into the String.

Another method is using the string slicing method. Slice the string before the character you want to update, then add the new character and finally add the other part of the string again by string slicing.

Example:

In this example, we are using both the list and the string slicing method to update a character. We converted the String1 to a list, changes its value at a particular element, and then converted it back to a string using the Python string join() method.

In the string-slicing method, we sliced the string up to the character we want to update, concatenated the new character, and finally concatenate the remaining part of the string.





string1="Hello, I'm a Ujjwala"
#UJJWALA
        #-6 -5 -4 -3 -2 -1
#print(string[::0])

#print(string[1:5:0])
#print(string[5:9:2])

#result=" ".join(string)
#print(result)

list1=list(string1)
#print(type(list1))

list1[8]=' a'
string2=''.join(list1)
print(string2)

Hello, I am a Ujjwala

method:-2

string1="Hello, I'm a Ujjwala"
string3=string1[0:8]  +' a'+string1[9:]
print(string3)
output

Hello, I am a Ujjwala


Formatting of Strings
Strings in Python or string data type in Python can be formatted with the use of format() method which is a very versatile and powerful tool for formatting Strings. Format method in String contains curly braces {} as placeholders which can hold arguments according to position or keyword to specify the order.

String1 = "{2}".format('Python', 'For', 'Life')
print(String1)
o/p
Life


Q: sort the words in alphabetic 

Words="This is my sentence"
Out="is my sentence this"


num='123'
print(num.isdigit())

True


string="hello"
repeated=0
repated_char=[]
for i in string:

    if(string.count(i)>1) and (i not in repated_char):
        repeated +=1
        repated_char.append(i)
print(repated_char)
print(repeated)

output:-
['l']
1
