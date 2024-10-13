------------------------------>get in python<----------------------------------------

In Python, get is commonly used in the context of dictionaries. It is a method that allows you to retrieve a value associated with a specified key, 
with the option of providing a default value if the key doesn't exist in the dictionary. This makes it safer than directly accessing dictionary keys with 
square brackets ([]), as it won't raise a KeyError if the key isn't present.


Syntax:-

dictionary.get(key, default_value)


* key: The key whose value you want to retriev
* default_value: (Optional) The value to return if the key is not found in the dictionary. If omitted, it defaults to None.

my_dict = {'a': 1, 'b': 2, 'c': 3}

print(my_dict.get('a'))
print(my_dict.get('b'))
print(my_dict.get('d'))

output:

1
2
None


This method is especially useful when you want to avoid handling exceptions for missing keys and instead provide a fallback value.

more examples below

1. Basic Usage with Default Values
# Example dictionary
person = {'name': 'Alice', 'age': 30}

# Retrieve an existing key
print(person.get('name'))  # Output: Alice

# Retrieve a non-existing key with a default value
print(person.get('gender', 'Not specified'))  # Output: Not specified

# Retrieve a non-existing key without a default value
print(person.get('address'))  # Output: None

2. Using get to Avoid KeyError

Using get helps avoid KeyError that would be raised if you use square brackets ([]) to access a non-existing key

# Using square brackets (causes KeyError if key doesn't exist)
# print(person['gender'])  # This would raise a KeyError

# Using get avoids the error
print(person.get('gender'))  # Output: None


3. Default Value as a Fallback Mechanism

# A dictionary representing inventory
inventory = {'apples': 5, 'oranges': 10}

# Check the stock of bananas with a default value of 0 if not found
print(inventory.get('bananas', 0))  # Output: 0

# Check the stock of apples (existing key)
print(inventory.get('apples', 0))  # Output: 5


4. Using get with Conditional Logic

get is often used with conditions to handle missing values more gracefully.

# User input represented as a dictionary
user_input = {'username': 'john_doe'}

# Set a default welcome message if the key 'welcome_message' is not provided
welcome_message = user_input.get('welcome_message', 'Hello, Guest!')
print(welcome_message)  # Output: Hello, Guest!

# If the 'welcome_message' key existed, it would use that value instead.
user_input['welcome_message'] = 'Welcome back, John!'
print(user_input.get('welcome_message', 'Hello, Guest!'))  # Output: Welcome back, John!


5. Nested Dictionaries with get


user_profile = {
    'name': 'John',
    'location': {'city': 'New York', 'country': 'USA'}
}

print(user_profile.get('location',{}))
user=user_profile.get('location',{}).get('city')

print(user)

user_na=user_profile.get('location',{}).get('zipcode','Not defined')

print(user_na)




