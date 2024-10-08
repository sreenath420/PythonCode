------------------------------------------------------------>1.Find Missing Number<----------------------------------------------------------

list=[2,5,6,7,10]
o/p:=[3, 4, 8, 9]


code:-

list=[2,5,6,7,10]
def missing(list):
    missing_number=[]
    for i in range(list[0],list[-1]):
        if i not in list:
            missing_number.append(i)
    return missing_number

print(missing(list))


------------------------------------------------------>2.Sum of two Numbers <-------------------------------------------------------------
def targetTwo(nums,target):
    m={}
    for i in range(len(nums)):
        num=nums[i]
        reaming=target -num
        if reaming in m:
            return [m[reaming],i]
        m[num]=i


nums=[4,6,9,2,3,4,5,12]
target=10
print(targetTwo(nums,target))


---------------------------------------------------------->3.partition the list based on given number<------------------------------------------------------
list = [1,2,99,8,77,66,54,67,80,45,32,27]
partition_num=40
def partition_fun(list,partition_num):
    min_value=[]
    max_value=[]
    for i in list:
        if i < partition_num:
            min_value.append(i)
        else:
            max_value.append(i)
    return min_value+max_value

print(partition_fun(list,partition_num))

--------------------------------------------------------------------->4.Remove_duplicates in given list<-------------------------------------------------------

list=[1,2,3,3,4,5,5,5,6,6]
output=[1, 2, 3, 4, 5, 6]
def remove_duplicate(list):
    remove_values=[]
    for i in list:
        if i not in remove_values:
            remove_values.append(i)
    return remove_values


print(remove_duplicate(list))


---------------------------------------------------->5.pattern matching<----------------------------------------------
for i in range(6):
  for j in range(i):
    print(i,end='')
  print('')

---------------------------------------------------->6.moving zeros<-------------------------------------------------------
method:-1
num=[6,7,0,9,0,3,3,4,5,0]
output:-[6, 7, 9, 3, 3, 4, 5, 0, 0, 0]

def moveZeros(num):
    j =0
    for i in range(len(num)):
        if num[i]!=0:
            num[j]=num[i]
            j +=1
    for k in range(j,len(num)):
        num[k]=0
    return num
print(moveZeros(num))
method:-2


list1=[k for k in num if k!=0]
list2=[k for k in num if k==0]
print(list1+list2)

method:-3
its best soluation 
num=[6,7,0,9,0,3,3,4,5,0]

def moveZeros(num):
    r=0
    for i in range(len(num)):
        if num[i]:
            num[r],num[i]=num[i],num[r]
            r +=1
    return num

print(moveZeros(num))

--------------------------------------------->7.count the each word in given string<----------------------------------------------------

pharse = "big black bug bit a big black dog on his on big black nose"

result=pharse.split()
#print(result)

def count_numbers(result):
    count_num={}
    for i in result:
        if i in count_num:
            count_num[i] +=1
        else:
            count_num[i]=1
    return count_num
print(count_numbers(result))

output:-

{'big': 3, 'black': 3, 'bug': 1, 'bit': 1, 'a': 1, 'dog': 1, 'on': 2, 'his': 1, 'nose': 1}


------------------------------------------>8.count the repeated letter<---------------------------------------------------
result = "aabbccddeeffhg"

def count_numbers(result):
    count_num={}
    for i in result:
        if i in count_num:
            count_num[i] +=1
        else:
            count_num[i]=1
    return count_num
print(count_numbers(result))
output:-
{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'h': 1, 'g': 1}

------------------------------------------>9.count the number each in the list<------------------------------------------------------

num=[2,3,3,3,4,4,5,5,6,6,7,7]
def count_number(num):
    result={}
    for i in num:
        if i in result:
            result[i] +=1
        else:
            result[i]=1
    return result

print(count_number(num))

output:-
{2: 1, 3: 3, 4: 2, 5: 2, 6: 2, 7: 2}


------------------------------------------------>10.is_subsequence<-----------------------------------------------------------------------------

def is_subsequence(s,t):
    i=j=0
    while i < len(s) and j < len(t):
        if s[i]==t[j]:
            i +=1
        j +=1
    return i==len(s)

s1 = "abc"
s2 = "sagfhdbdsrgcadsf"
print(is_subsequence(s1,s2))

output:-
True

--------------------------------------------------->11.count_word_prefix<----------------------------------------------------------------------
words=["bilingual", "macroeconomics", "enlarge", "macroscopic", "monolingual"]
prefix="macro"

def word_prefix(words,prefix):
    counter = 0
    for i in range(len(words)):
        word_prefix=words[i][:len(words)]
        if word_prefix==prefix:
            counter +=1
    return counter
print(word_prefix(words,prefix))

ouput:-
2

--------------------------------------------------------->12.Count Word Frequency<-------------------------------------------------------------------


words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 
Output: {'apple': 3, 'orange': 2, 'banana': 1}

def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
------------------------------------------------------->13.merge two dictionaries in python<------------------------------------------------------------

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

for k,v in dict2.items():
    dict1[k]=dict1.get(k,0)+v
print(dict1)


output:-
{'a': 1, 'b': 5, 'c': 7, 'd': 5}


--------------------------------------------------->14.Merge Strings Alternately<---------------------------------------------------------------

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r


Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=j=0
        result=""
        while i < len(word1) and j < len(word2):
            result +=word1[i]+word2[j]
            i +=1
            j +=1
        while i < len(word1):
            result +=word1[i]
            i +=1
        while j < len(word2):
            result +=word2[j]
            j +=1
        return result

----------------------------------------------->15.substring_index<---------------------------------------------------


str = "abracabrdabaacdefabr"
substr = "abr"
lst = []
for i in range(0,len(str)):
    if str[i:i+len(substr)] == substr:
        lst.append(i)
print(lst)
o/p
[0, 5, 17]


---------------------------------------------->16.Prime_Number<----------------------------------------------------------------

#checking given number is prime or not
given_number = 9999991

def primeNumber(givnum):
    strout = ""
    for i in range(2,givnum):
       if givnum % i == 0:
           strout = "Given is not a prime"
           break
    else:
        strout = "Given is prime"
    return strout

print(primeNumber(given_number))


------------------------------------>17.flattend list<-------------------------------------------------------------

#Flatten nested list
lst = [[1,2,3,4,5],[6,7,8,9],'a','b',10,11]
flatten_list = []

def flattenStrings(lst): ## it will flattten integer and string both
    for i in lst:
        if isinstance(i,list):
            flatten_list.extend(i)
            #exted will add antoher list here its comes [1, 2, 3, 4, 5, 6, 7, 8, 9]
        else:
            flatten_list.append(i)
    return flatten_list

print(flattenStrings(lst))

output:-
[1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 10, 11]


----------------------------------->18.Nested_Keys<---------------------------------------------------------

nested_dict = {'a': {'b': {'c': 42}}}
keys = ['a', 'b', 'c','d']
#output:-42

def nested_dict1(nested_dict,keys):
        for i in keys:
            if isinstance(nested_dict, dict) and i in nested_dict:
                nested_dict=nested_dict[i]
        #print(nested_dict)
        return nested_dict

print(nested_dict1(nested_dict,keys))


-------------------------------------->19.Prime_numbers<------------------------------------------
given_number = 9999991

def primeNumber(givnum):
    strout = ""
    for i in range(2,givnum):
       if givnum % i == 0:
           strout = "Given is not a prime"
           break
    else:
        strout = "Given is prime"
    return strout

print(primeNumber(given_number))

-------------------------------------->20.𝗪𝗿𝗶𝘁𝗲 𝗮 𝗣𝘆𝘁𝗵𝗼𝗻 𝗽𝗿𝗼𝗴𝗿𝗮𝗺 𝘁𝗼 𝗴𝗲𝘁 𝘁𝗵𝗲 𝗹𝗲𝗻𝗴𝘁𝗵 𝗼𝗳 𝘁𝗵𝗲 𝗶𝗻𝗽𝘂𝘁 𝘀𝘁𝗿𝗶𝗻𝗴𝘀 𝗮𝗻𝗱 𝗰𝗼𝘂𝗻𝘁 𝗲𝗮𝗰𝗵 𝗰𝗵𝗮𝗿𝗮𝗰𝘁𝗲𝗿 𝗼𝗰𝗰𝘂𝗿𝗿𝗲𝗻𝗰𝗲 𝗲𝘅𝗰𝗹𝘂𝗱𝗶𝗻𝗴 𝘀𝗽𝗮𝗰𝗲𝘀<------------------------------------------
text = "apple banana apple orange banana apple orange apple"
words=text.replace(" ","")

print(words)

words_count={}
for word in words:
    #print(len(words))
    if word in words_count:
        words_count[word] +=1
    else:
        words_count[word]=1
print((len(words),words_count))

----------------------------------->21.weighted_list<---------------------------------------------------------------------

dict1={1:"apple", 2:"orange", 3:"peer"}
li=["apple","orange","peer"]

def countS(s):
    count=0
    for i in s:
        count +=ord(i)
    return count

def dict_weight(dict1):
    weight_list={}
    for i,v in dict1.items():
        cnt_count=countS(v)
        weight_list[v]=cnt_count
    return weight_list

print(dict_weight(dict1))

output
{'apple': 530, 'orange': 636, 'peer': 428}

-------------------------------------------->22.Anagrams Problems<--------------------------------------------------------------------
                                 --->a.Group_anagram<---
what is anagram
An anagram is a word, phrase, or name formed by rearranging the letters of another word, 
phrase, or name, typically using all the original letters exactly once. For example, 
the word "listen" can be rearranged to form the word "silent." Anagrams are often used in word games and puzzles.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_list={}
        for word in strs:
            key=''.join(sorted(word))
            if key not in anagram_list:
                anagram_list[key]=[word]
            else:
                anagram_list[key].append(word)
        return list(anagram_list.values())

                        ---->b.Valid Anagram<----

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

 def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)


------------------------------------------>23.GCD calculation<--------------------------------------------

#Find GCD = Greatest Common Divisor in a given list 
def findGcd(a,b):
    while b:  # stops when b = 0
        #print(b)
        a,b = b, a%b #56,42 = 42,14 #
    return a

def gcd_list(nums):
    gcd_result = nums[0]
    for num in nums[1:]:
        gcd_result = findGcd(gcd_result,num)
    return gcd_result

nums = [42,56,14,84]

result = gcd_list(nums)
print(f"The GCD of the list {nums} is: {result}")

-------------------------------------->24.𝗣𝘂𝘁 𝘁𝗵𝗲 𝗻𝗲𝗴𝗮𝘁𝗶𝘃𝗲 𝘃𝗮𝗹𝘂𝗲𝘀 𝗮𝘁 𝘁𝗵𝗲 𝗲𝗻𝗱 𝗼𝗳 𝘁𝗵𝗲 𝗹𝗶𝘀𝘁 𝗼𝗿𝗱𝗲𝗿 𝘀𝗵𝗼𝘂𝗹𝗱 𝗯𝗲 𝗺𝗮𝗶𝗻𝘁𝗮𝗻𝗶𝗻𝗲𝗱<----------------------------------------


tuples_list_1 = [(1, 'apple'), (-3, 'banana'), (2, 'cherry'), (-1, "Negative"), (-2, "Negarive_2")]
output:-[(1, 'apple'), (2, 'cherry'), (-3, 'banana'), (-1, 'Negative'), (-2, 'Negarive_2')]

code of the problem
# 𝗜𝗻𝗶𝘁𝗶𝗮𝗹𝗶𝘇𝗲 𝗮𝗻 𝗲𝗺𝗽𝘁𝘆 𝗹𝗶𝘀𝘁 𝘁𝗼 𝘀𝘁𝗼𝗿𝗲 𝘁𝗵𝗲 𝗿𝗲𝘀𝘂𝗹𝘁

tuple_add=[]
# 𝗜𝘁𝗲𝗿𝗮𝘁𝗲 𝘁𝗵𝗿𝗼𝘂𝗴𝗵 𝘁𝗵𝗲 𝗼𝗿𝗶𝗴𝗶𝗻𝗮𝗹 𝗹𝗶𝘀𝘁

for i in range(len(tuples_list_1)):
    if tuples_list_1[i][0] <0:
        tuple_add.append(tuples_list_1[i])
# 𝗥𝗲𝗺𝗼𝘃𝗲 𝘁𝗵𝗲 𝗻𝗲𝗴𝗮𝘁𝗶𝘃𝗲 𝘁𝘂𝗽𝗹𝗲𝘀 𝗳𝗿𝗼𝗺 𝘁𝗵𝗲 𝗼𝗿𝗶𝗴𝗶𝗻𝗮𝗹 𝗹𝗶𝘀𝘁


tuples_list_1=[t for t in tuples_list_1 if t[0]>=0]
# 𝗔𝗽𝗽𝗲𝗻𝗱 𝘁𝗵𝗲 𝗻𝗲𝗴𝗮𝘁𝗶𝘃𝗲 𝘁𝘂𝗽𝗹𝗲𝘀 𝘁𝗼 𝘁𝗵𝗲 𝗲𝗻𝗱 𝗼𝗳 𝘁𝗵𝗲 𝗼𝗿𝗶𝗴𝗶𝗻𝗮𝗹 𝗹𝗶𝘀𝘁

tuples_list_1.extend(tuple_add)

print(tuples_list_1)






