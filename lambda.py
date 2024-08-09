--------------------------------------------------------------->Lambda functions in python<---------------------------------------------------------------
A lambda function in Python is a small anonymous function defined using the lambda keyword. Lambda functions are often used for short-lived operations or when you need a simple function for a short period.

Syntax:-
lambda arguments: expression

lambda: The keyword to define the lambda function.
arguments: A comma-separated list of arguments (parameters) the function takes.
expression: A single expression that is evaluated and returned by the function.

example:-1

add_ten=lambda x:x+10

print(add_ten(4))

output:-14


2.using lambda with multiple arugments 

# A lambda function that multiplies two arguments
multiply = lambda x, y: x * y

print(multiply(4, 5))  # Output: 20


3.using lambda with sorted()

multiply = lambda x, y: x * y

print(multiply(4, 5))  

4.Using lambda with map()

# List of numbers
numbers = [1, 2, 3, 4]

# Square each number using map() and lambda
squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)  # Output: [1, 4, 9, 16]

5.Using lambda with filter()
# List of numbers
numbers = [1, 2, 3, 4, 5]

# Filter out even numbers using filter() and lambda
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)  # Output: [2, 4]


                   ---------------------------->key=lambda<-------------------------------
The key=lambda construct in Python is commonly used in functions like sorted(), max(), and min() to specify a custom sorting or comparison criterion. Lambda functions provide a concise way to define small, anonymous functions that can be used as the key for these operations.

Understanding key=lambda
1.Lambda Functions: A lambda function is a small anonymous function defined with the lambda keyword. It can take any number of arguments but only has one expression.
2.Key Parameter: The key parameter allows you to specify a function that extracts a comparison key from each element in the iterable. This is particularly useful for sorting complex data structures.

example of using 'key=lambda'

Sorting a list of Tuples

Suppose you a have list of tuples representing items with a name and a price,and you want to sort them by price.

items = [("apple", 2), ("banana", 1), ("cherry", 3)]

sort_items=sorted(items,key=lambda x:x[1])
print(sort_items)

output:
[('banana', 1), ('apple', 2), ('cherry', 3)]

Suppose you a have list of tuplse representing min values of given list

items = [("apple", 2), ("banana", 1), ("cherry", 3)]
In this example, the lambda function lambda x: x[1] extracts the price from each tuple, and sorted() uses these values to sort the list.

sort_items=min(items,key=lambda x:x[1])
print(sort_items)

output:-
('banana', 1)

Sorting a List of Dictionaries
You can also use key=lambda to sort a list of dictionaries based on a specific key:

users = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}]
dict_sorted=sorted(users,key=lambda x:x['age'])

print(dict_sorted)

output:-

[{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]



Here, the lambda function lambda user: user["age"] extracts the age from each dictionary, allowing sorted() to sort the users by age.


Concusion
Using key=lambda in Python provides a powerful and flexible way to customize sorting and comparisons. It allows you to define simple, inline functions that can be used to extract specific criteria from elements, making your code more concise and readable.