Certainly! Here are multiple questions for each of the mentioned topics: strings, arrays, lists, sets, and tuples. These questions range from basic to intermediate difficulty and are designed to help you practice and improve your problem-solving skills in these areas.

### Strings
1. *Palindrome Check*: Write a program to check if a given string is a palindrome.
2. *Anagram Check*: Write a function to determine if two strings are anagrams.
3. *String Compression*: Implement a method to perform basic string compression using the counts of repeated characters.
4. *First Unique Character*: Find the first non-repeating character in a string.
5. *String Permutations*: Generate all permutations of a given string.
6. *Longest Substring Without Repeating Characters*: Find the length of the longest substring without repeating characters.
7. *Count Vowels and Consonants*: Write a program to count the number of vowels and consonants in a string.
8. *Reverse Words in a String*: Reverse the order of words in a given string.
9. *String to Integer (atoi)*: Implement the atoi function to convert a string to an integer.
10. *String Rotation*: Check if one string is a rotation of another string.

### Arrays
1. *Find Duplicate*: Given an array of integers, find if the array contains any duplicates.
2. *Rotate Array*: Rotate an array of n elements to the right by k steps.
3. *Maximum Subarray*: Find the contiguous subarray within an array that has the largest sum.
4. *Merge Sorted Arrays*: Merge two sorted arrays into one sorted array.
5. *Two Sum*: Given an array of integers, return indices of the two numbers such that they add up to a specific target.
6. *Move Zeroes*: Move all zeroes in an array to the end while maintaining the relative order of the other elements.
7. *Find Missing Number*: Find the missing number in an array containing numbers from 1 to n.
8. *Product of Array Except Self*: Return an array such that each element is the product of all elements in the original array except the one at that index.
9. *Find Intersection*: Find the intersection of two arrays.
10. *Array Partition*: Given an array of 2n integers, group these integers into n pairs of integers, and maximize the sum of the minimum of each pair.

### Lists
1. *Remove Duplicates*: Remove duplicates from a list.
2. *Flatten Nested List*: Given a nested list of integers, flatten it into a single list.
3. *Merge Two Lists*: Merge two sorted lists into a single sorted list.
4. *List Comprehension*: Generate a list of squares of even numbers from 1 to 20.
5. *Partition List*: Given a list and a value x, partition it such that all elements less than x come before elements greater than or equal to x.
6. *Rearrange List*: Rearrange a list such that positive and negative numbers alternate.
7. *Rotate List*: Rotate a list to the right by k places.
8. *Sublist with Given Sum*: Find a sublist in a list that adds up to a given sum.
9. *Palindrome List*: Check if a list is a palindrome.
10. *Zip and Unzip*: Implement zip and unzip functions for lists.

### Sets
1. *Union and Intersection*: Perform union and intersection operations on two sets.
2. *Set Difference*: Find the difference between two sets.
3. *Symmetric Difference*: Find the symmetric difference between two sets.
4. *Subset Check*: Check if one set is a subset of another.
5. *Remove Duplicates from List*: Use a set to remove duplicates from a list.
6. *Count Unique Elements*: Count the number of unique elements in a list.
7. *Set Operations*: Write functions to perform set operations like union, intersection, difference, and symmetric difference.
8. *Find Common Elements*: Find common elements in three sets.
9. *Distinct Elements*: Find the distinct elements in a list using a set.
10. *Set Comprehension*: Use set comprehension to create a set of squares of numbers from 1 to 10.

### Tuples
1. *Swap Elements*: Swap two elements in a tuple.
2. *Find Element Index*: Find the index of an element in a tuple.
3. *Tuple Concatenation*: Concatenate two tuples.
4. *Convert List to Tuple*: Convert a list to a tuple.
5. *Nested Tuples*: Access elements from nested tuples.
6. *Tuple with Single Element*: Create a tuple with a single element.
7. *Unpack Tuple*: Unpack elements of a tuple into individual variables.
8. *Tuple of Lists*: Given a tuple of lists, sort each list.
9. *Find Max and Min*: Find the maximum and minimum elements in a tuple of numbers.
10. *Immutable Property*: Demonstrate the immutability of tuples by attempting to modify one.

These questions cover a variety of scenarios and operations you might need to perform with strings, arrays, lists, sets, and tuples. They should help you build a strong foundation in handling these data structures.















----------------------------------------------------------> factorial Number <--------------------------------------------------

try:
    num = int(input('Enter Number\t'))
    factorial = 1
    if num == 0:
        print("o/p is 1")
    elif num < 0:
        print("not exist")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print(factorial)

except ValueError:
    print("Error:Please enter a Valid Number")



--------------------------------------------------------->Fib number<-----------------------------------------------------------------------

try:

    n = int(input("Enter a Number"))
    a = 0
    b = 1

    if n == 0:
        print("not egligble for fib number")
    elif n == 1:
        print("Fib number is", b)

    else:
        count = 0
        while count < n:
            print(a)
            n1 = a + b
            a = b
            b = n1
            # n = a + b]
            count +=1
except ValueError:
    print("Enter the valid number")


