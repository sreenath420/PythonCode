-------------------------------------------------------------------->1<-------------------------------------------------------------------------
1.Remove Duplicate values in given list 

list=[1,2,4,4,5,6,6,7,7]


def remove_duplicates(list):
result=[]
for i in list:
   if i not in result:
      result.append(i)
return result
----------------------------------------------------------------->2<------------------------------------------------------------------------------
2.Write a python function dict_sort_by_value(dict) so that for given dictionary, it will return the dictionary with sort by value.
example 
input: dict = {1001:'A', 1002:'B', 1003:'A', 1004:'C',  1005:'B',   1006:'C'}
output: {1001:'A', 1003:'A', 1002:'B', 1005:'B', 1004:'C', 1006:'C'}

sorted_footballers_by_goals = sorted(footballers_goals.items(),key= lambda x:x[1])
------------------------------------------------------------------->3<-------------------------------------------------------------------------------
3.write python program to get repeted value which value repeatec 3 times here
output:-
comm_value [2, 6]

li=[1,2,3,4,6,7,8,9,9,0,8,0,2,2,6,6,87,65,34,23]
count_dict ={}
for num in li:
    if num in count_dict:
        count_dict[num] +=1
        #print(count_dict)
    else:
        count_dict[num] =1
#print(count_dict)
comm_values=[num for num,count in count_dict.items() if count==3]
print('comm_value',comm_values)

method:-2

def count_dict(li,repetition_count=3):
    dict_cnt={}
    for i in li:
        if i  not in dict_cnt:
            dict_cnt[i]=1
        else:
            dict_cnt[i] +=1
    nn=[num for num,count in dict_cnt.items() if count==repetition_count]
    return nn
print(count_dict(li))

method:-3

li=[1,2,3,4,6,7,8,9,9,0,8,0,2,2,6,6,87,65,34,23]

count_dict={}
for n in li:
    count_dict[n]=count_dict.get(n,0)+1

print(count_dict)
---------------------------------------------------------------------->4<--------------------------------------------------------------------
4.write python repeat the letter give string
word="fdcaagahaajqaa"
counter={}
for letter in word:
    if letter not in counter:
        counter[letter]=0
    counter[letter] +=1
print(counter)
o/p
{'f': 1, 'd': 1, 'c': 1, 'a': 7, 'g': 1, 'h': 1, 'j': 1, 'q': 1}


2nd way 

word="fdcaagahaajqaa"
counter={}
for letter in word:
    counter[letter]=counter.get(letter,0)+1
print(counter)

------------------------------------------------------------------------->5<---------------------------------------------------------------------------------
5.Find the largest pair sum in an array in python by using for loop
Method:-1
def largest_pair_sum(arr):
    # Initialize variables to store the largest and second-largest elements
    max1 = 0
    max2 = 0

    # Iterate through the array to find the largest and second-largest elements
    for num in arr:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    # Return the sum of the largest and second-largest elements
    return max1, max2

# Example usage:
array = [3, 6, 2, 8, 10, 5,15]
max_pair_sum = largest_pair_sum(array)
print("Largest pair sum:", max_pair_sum)

Method:-2
def largest_pair_sum(arr):
    # Sort the array in ascending order
    arr.sort()
    print(arr[-1],arr[-2])
    # Return the sum of the last two elements
    return arr[-1],arr[-2]


# Example usage:
array = [3, 6, 2, 8, 10, 5,15]
max_pair_sum = largest_pair_sum(array)
print("Largest pair sum:", max_pair_sum)

------------------------------------------------------------>6.count the words<------------------------------------------------------------------------------------
6
phrase = "big black bug bit a big black dog on his on big black nose"
words=phrase.split()
print(words)

word_count={}

for word in words:
        if word in word_count:
                word_count[word] +=1

                #print(word_count)
        else:
                word_count[word]=1
for val,count in word_count.items():
        print(val,count)

-------->2nd way of code<----


words=phrase.split()
print(words)

word_count={}

for counts in words:
    word_count[counts]=word_count.get(counts,0)+1
print(word_count)

output
------
big 3
black 3
bug 1
bit 1
a 1
dog 1
on 2
his 1
nose 1


----------------------------------------->7.problem<--------------------------------------------------------------------
7
you are given an array of N inetegers. you want to split them into N/2 pairs in such a way that the sum of integers in each pair is odd. N is even and every element of the array
must be present in exactly one pair
you task is to determine whether it is possible to split the numbers into such pairs.for example,given[2,7,4,6,3,1], The answer is True
one of the possible sets of pairs is (2,7),(6,3) and (4,1) Theirs sums are respectively 9,9 and 5 all of which are odd.

example
1.given A=[2,,7,4,6,3,1] the function should return True,
2.given A=[1,1] the function should return False
3.given A=[2,1] the function shoudl return True



def soluation(A):
    count_even=0
    for n in A:
        if n %2==0:
            count_even +=1
    count_odd=len(A) - count_even
    if count_odd !=count_even:

        return False
    return True


print(soluation([2,7,4,6,3,1]))
print(soluation([1,1]))
print(soluation([2,1]))





output:-

True
False
True



----------------------------------------------------------------->8.is_subsequence<---------------------------------------------------------------------------
8.
def is_subsequence(s,t):
    i=j=0
    while i < len(s) and j < len(t):
        if s[i]==t[j]:

            #print(s[i],t[j])
            i += 1


        j +=1

    return i==len(s)

s1 = "abc"
s2 = "sagfhdbdsrgcadsf"
s3="abc"
s4="sgfhdbdsrgcadsf"
print(is_subsequence(s1,s2))

True
False


count the each number occurence in a give list

-------------------------------------------------------------->9<-----------------------------------------------------------------------
9.duplicate = [12,11,12,14,12,13,20,19,4,5,4,3,6,9]

{12: 4, 11: 1, 14: 2, 13: 1, 20: 1, 4: 2, 5: 1, 3: 1, 9: 1}

#print(set(duplicate))

dupl={}
for i in duplicate:
    if i in dupl:
        dupl[i] +=1
    else:
        dupl[i]=1

print(dupl)

method:-2
out={}

for num in duplicate:
    out[num]=out.get(num,0)+1
print(out)
--------------------------------------->10.weight of the give dicti<------------------------------------------
10.
dict={1:"apple", 2:"orange", 3:"peer"}


def calculate_values(a):
    weight = 0
    for char in a:
        weight +=ord(char)
    return weight

def assign_weighted(dict):
    weighted_dict={}
    for key,value in dict.items():
        weight=calculate_values(value)
        weighted_dict[value]=weight
    return  weighted_dict

print(assign_weighted(dict))


output:-

{'apple': 530, 'orange': 636, 'peer': 428}
--------------------------------------------->11.sotred list based on string value<-------------------------------------------
11.
Bubble sort
input:-str=["walk","swim","run","jump","dance"]
output:- ['dance', 'jump', 'run', 'swim', 'walk']


str=["walk","swim","run","jump","dance"]
def buble_sorted(str):
    n =len(str)
    print(n)
    for i in range(n):
        #print(str[i])
        for j in range(n-i-1):#-->4
            if str[j]>str[j+1]:
                str[j],str[j+1]=str[j+1],str[j]
    return str
print(buble_sorted(str))


o/p:-

['dance', 'jump', 'run', 'swim', 'walk']


------------------------------------------------------12.Target of two sums----------------------------------------------------------------------------------

12.
Input-
num=[4,6,7,2,3]
target=10

Output-
[0,1]

num=[4,6,7,2,3]
target =10
def twoTarget(num,target):
    m={}
    for i in range(len(num)):
        nums=num[i]
        rem=target-nums
        if rem in m:
            #print(m)
            return [m[rem],i]
        m[nums]=i

print(twoTarget(num,target))

----------------------------------------------------------13.count of substring----------------------------------------------------------------------
13.
input-
a="ababababa"  
b="aba"
output-
4
a="ababababa"  
b="aba"
c=0
for i in range(0,len(a)):
    if a[i:i+len(b)]==b:
       c+=1
print(c)

----------------------------------------------------14.Anagram-----------------------------------------------------------------------------------------

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

strs=["eat","tea","tan","ate","nat","bat"]
def anagram_list(strs):
    anagram_values={}
    for word in strs:
        key = ''.join(sorted(word))
        print(key)
        if key not in anagram_values:
            anagram_values[key]=[word]
            print("not append vale",anagram_values)
        else:
            anagram_values[key].append(word)
            print("append values",anagram_values)
    return list(anagram_values.values())

print(anagram_list(strs))

--------------------------------------------------------15.flattend_list-------------------------------------------------------------------------------------

lst = [[1,2,3,4,5],[6,7,8,9],'a','b',[10,11]]
output=[1,2,3,4,5,6,7,8,9,'a','b',10,11]
result=[]
for i in lst:
  if isinstance(i,list):
    result.extend(i)
  else:
    result.append(i)  
print(result)

def flattend_list(result):
  result=[]
  for i in lst:
    if isinstance(i,list):
      result.extend(i)
    else :
      result.append(i)
  return result
lst = [[1,2,3,4,5],[6,7,8,9],'a','b',[10,11]]
print(flattend_list(lst)) 

--------------------------------------------------------16.count_consecutive_characters-------------------------------------------------------------------------------------
inpput-
ujjwala
output-
u1j2w1a1l1a1
def count_consecutive_characters(input_string):
    result=''
    count=1
    pre_char=input_string[0]
    for char in input_string[1:]:
        if char==pre_char:
            count +=1
        else:
            result +=f"{pre_char}{count}"
            count =1
            pre_char=char
    result +=f"{pre_char}{count}"
    return result
input_string='ujjwala'
print(count_consecutive_characters(input_string))


--------------------------------------------------------17.Print only values not any keys-------------------------------------------------------------------------------------

nested_dict = {'a': {'b': {'c': 42}}}
keys = ['a', 'b', 'c']
output:- 42
Method 1--------------------------------------------------------
nested_dict = {'a': {'b': {'c': 42}}}
keys = ['a', 'b', 'c']

def nested_func(nested_dict,keys):
    for i in keys:
        nested_dict=nested_dict[i]
    return  nested_dict
print(nested_func(nested_dict,keys))

Method 2---------------------------------------------------------
nested_dict = {'a': {'b': {'c': 42}}}

for k,v in nested_dict.items():
    #print(v)
    for i,j in v.items():
        #print(j)
        for k,x in j.items():
            print(x)

-------------------------------------->18.print common values between two lists<----------------------------------------------
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
out=[3,4]

result=[x for x in list1 if x in list2]
print(result)


----------------------------------->19.count the each letter in given string<----------------------------------
count the vowels in given string
input
name = 'SrEenath'
output
e 2
a 1
def count_vowels(name,vowels):
    # Initialize an empty dictionary to store individual character counts
    dict_individual = {}

    # Count each character in the string
    for i in name.lower():
        if i in dict_individual:
            dict_individual[i] += 1
        else:
            dict_individual[i] = 1

    # Define the vowels
    #vowels = 'AEIOUaeiou'

    # Print the counts of only the vowels

    for key, value in dict_individual.items():
        if key in vowels:
            print(key, value)

# Example usage
name = 'SrEenath'
vowels = 'AEIOUaeiou'
count_vowels(name,vowels)


------------------------------------->20.Flattend_List<--------------------------------------------------------
input:-
lis=[1,2,3,[4,5],6,[7,8,[9,2]],10]
output:-
[1, 2, 3, 4, 5, 6, 7, 8, 9, 2, 10]

lis=[1,2,3,[4,5],6,[7,8,[9,2]],10]

def flattend(lis):
    flatted_list=[]
    for num in lis:
        if isinstance(num,list):
            flatted_list.extend(flattend(num))
        else:
            flatted_list.append(num)
    return flatted_list


print(flattend(lis))


------------------------------------------------>21.List Comprehension <------------------------------------------------------------
make a list , based on list a where 1 is for odd, 0 is for even
num=[22,57,34,96,59,65,98]

output
[0, 1, 0, 0, 1, 1, 0]

n1=[0 if i %2==0 else 1 for i in num]

print(n1)

--------------------------------------------->22.count the number of words each line<----------------------------------------------------

lines = [
    "ABC,DEF,GHI",
    "PPP,DDD"
]

for i,coun in enumerate(lines,start=1):
   words=coun.split(',')
   line=len(words)
   print(f"count the number of {i} words in each {line}")

output:-

count the number of 1 words in each 3
count the number of 2 words in each 2

------------------------------------------->23.covert dictionary to json in python<-----------------------------------------------
import json

# Sample dictionary
data = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Convert dictionary to JSON string
json_string = json.dumps(data)

# Print the JSON string
print(json_string)
output:-

{"name": "Alice", "age": 30, "city": "New York"}

---------------------------------------->24.Anagram is true or not<------------------------------------------------------

def anagram(str1, str2):
    # Remove spaces, punctuation, and convert to lowercase
    str1 = ''.join(e for e in str1 if e.isalnum()).lower()
    str2 = ''.join(e for e in str2 if e.isalnum()).lower()
    #print(str2)

    # Check if sorted characters of both strings are equal
    return sorted(str1) == sorted(str2)


# Now, test the function with your example
result = anagram("The Morse Code", "Here come dots@!")
print(result)  # This will output: True

output:-
True


----------------->25.
You are given an array of N integers. You want to split them into N/2 pairs in such a way that the sum of integers in each pair is odd. N is even and every element of the array must be present in exactly one pair. Your task is to determine whether it is possible to split the numbers into such pairs. For example, given (2, 7, 4, 6, 3, 1], the answer is True. One of the possible sets of pairs is (2, 7), (6, 3) and (4, 1). Their sums are respectively 9, 9 and 5, all of which are odd.
 Write a function:
def solution(A)
which, given an array of integers A of length N, returns True when it is possible to create the required pairs and False otherwise.
 Examples:
1. Given A = [2, 7, 4,6, 3, 1], the function should return True, as explained above,.
2. Given A = [-1, 1], the function should return False. The only possible pair has the sum -1 + 1 = 0 which is even. 3. Given A = [2, -1], the function should return True. The only pair has sum -1 + 2 = 1, which is odd, 4. Given A = [1, 2, 4, 3], the function should return True. Possible pairs are (1, 2), (4, 3). They both have an odd sum 5. Given A = [-1, 3, 4, 7, 7, 7), the function should return False We can create only one pair with an odd sum by taking 4 and any of the other numbers: for example, 4 + 7 = 11 Al the other pairs have an even sum
 Write an efficient algorithm for the following assumptions <-----------------

input_list = [2,5,6,0,1]


def solution(A):
    # Count odd and even numbers
    odd_count = 0
    even_count = 0

    for num in A:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    # Check if the number of odd and even numbaers is equal
    return odd_count == even_count
print(solution(input_list))

-------------------------->26.create a function find the index of a number in a list in Python using sorting, here's how you can do it <------------------

def find_index_in_sorted_list(numbers, target_number):
    # Sort the list without modifying the original list
    sorted_numbers = sorted(numbers)

    # Find the index of the target number in the sorted list
    if target_number in sorted_numbers:
        index_in_sorted = sorted_numbers.index(target_number)
        return index_in_sorted
    else:
        return -1  # If the target number is not found in the list


# Example usage:
numbers = [50, 30, 10, 40, 20]
target_number = 30

index = find_index_in_sorted_list(numbers, target_number)
print(f"Index of {target_number} in the sorted list: {index}")


output:-

Index of 30 in the sorted list: 2


------------------------------------------------------>27.find the max word occurence in given string<------------------------------------------------------


name='i am sreenath i am doing good i am going to travel I'
#name=name.lower().split(' ')
name_split=name.lower().split(' ')
print(name_split)
names_words={}
for i in name_split:
    if i in names_words:
        names_words[i] +=1
    else:
        names_words[i]=1
print(names_words)


max_word = ''
max_count = 0

for word, count in names_words.items():
    if count > max_count:
        max_count = count
        max_word = word
print(max_word,max_count)
ouptut
i 4

----->28.Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct<---------
 
Example 1:
Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.
Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.
Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

def containsDuplicates(nums):
    seen=set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False
    
nums=[1,2,3]

print(containsDuplicates(nums))
output
    False

---------------------------------------------------------->29<--------------------------------------------------------------
input = ["john", "johnny", "juli", "john", "juli", "john"]
output = ["john_1", "johnny_1", "juli_1", "john_2", "juli_2", "john_3"]


def assign_counts(input_list):
    counts = {}
    output = []

    for name in input_list:
        #print(name)
        counts[name] = counts.get(name, 0) + 1

        output.append(f"{name}_{counts[name]}")
    return output


print(assign_counts(input))

output :-
   ['john_1', 'johnny_1', 'juli_1', 'john_2', 'juli_2', 'john_3']


--------------------------------->30.non-repeative char in given string<----------------------------------------

s = 'abcabcdefggh'


# Use a set to track seen characters and a   list for the result to maintain order
result=[char for char in s if s.count(char)==1]
s=''.join(result)

print(s)

output:-
defh

--------------------------->31.occurance character count<-----------------------------------------
input:-
str = 'aabbccabc'
output:-
a2b2c2
   
char_count={}
i=0
while i<len(str):
    char_current=str[i]
    count =1
    while i +1 <len(str) and str[i+1] ==char_current:
        count +=1
        i +=1
    if count >1:

        char_count[char_current]=count
    i +=1

output=''.join(f"{char}{count}" for char,count in char_count.items())
print(output)


