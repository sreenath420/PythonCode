------------------------------------------------------------>Find Missing Number<----------------------------------------------------------

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


------------------------------------------------------>Sum of two Numbers <-------------------------------------------------------------
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


---------------------------------------------------------->partition the list based on given number<------------------------------------------------------
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

--------------------------------------------------------------------->Remove_duplicates in given list<-------------------------------------------------------

list=[1,2,3,3,4,5,5,5,6,6]
output=[1, 2, 3, 4, 5, 6]
def remove_duplicate(list):
    remove_values=[]
    for i in list:
        if i not in remove_values:
            remove_values.append(i)
    return remove_values


print(remove_duplicate(list))


---------------------------------------------------->pattern matching<----------------------------------------------
for i in range(6):
  for j in range(i):
    print(i,end='')
  print('')

---------------------------------------------------->moving zeros<-------------------------------------------------------
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

--------------------------------------------->count the each word in given string<----------------------------------------------------

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


------------------------------------------>count the repeated letter<---------------------------------------------------
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

------------------------------------------>count the number each in the list<------------------------------------------------------

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


------------------------------------------------>is_subsequence<-----------------------------------------------------------------------------

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

--------------------------------------------------->count_word_prefix<----------------------------------------------------------------------
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

--------------------------------------------------------->Count Word Frequency<-------------------------------------------------------------------


words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
count_word_frequency(words) 
Output: {'apple': 3, 'orange': 2, 'banana': 1}

def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count
------------------------------------------------------->merge two dictionaries in python<------------------------------------------------------------

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

for k,v in dict2.items():
    dict1[k]=dict1.get(k,0)+v
print(dict1)


output:-
{'a': 1, 'b': 5, 'c': 7, 'd': 5}


--------------------------------------------------->Merge Strings Alternately<---------------------------------------------------------------

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

----------------------------------------------->substring_index<---------------------------------------------------


str = "abracabrdabaacdefabr"
substr = "abr"
lst = []
for i in range(0,len(str)):
    if str[i:i+len(substr)] == substr:
        lst.append(i)
print(lst)
o/p
[0, 5, 17]




