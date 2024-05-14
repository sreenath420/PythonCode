---------------------------------------------------------------------------------------------------------------------------------------------
1.Remove Duplicate values in given list 

list=[1,2,4,4,5,6,6,7,7]


def remove_duplicates(list):
result=[]
for i in list:
   if i not in result:
      result.append(i)
return result
-----------------------------------------------------------------------------------------------------------------------------------------------
2.Write a python function dict_sort_by_value(dict) so that for given dictionary, it will return the dictionary with sort by value.
example 
input: dict = {1001:'A', 1002:'B', 1003:'A', 1004:'C',  1005:'B',   1006:'C'}
output: {1001:'A', 1003:'A', 1002:'B', 1005:'B', 1004:'C', 1006:'C'}

sorted_footballers_by_goals = sorted(footballers_goals.items(),key= lambda x:x[1])
--------------------------------------------------------------------------------------------------------------------------------------------------
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

-----------------------------------------------------------------------------------------------------------------------------------------------------
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

----------------------------------------------------------------------------------------------------------------------------------------------------------
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

------------------------------------------------------------>count the words<------------------------------------------------------------------------------------
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


----------------------------------------->problem<--------------------------------------------------------------------
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



----------------------------------------------------------------->is_subsequence<---------------------------------------------------------------------------
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

--------------------------------------> Target of two Sums<-----------------------------------------------------------------
9.
def targetSum(nums):
    target = 10
    m = {}
    for i in range(len(nums)):
        num = nums[i]
        #print(num)
        reaminder = target - num #----> 10-4=6
        if (reaminder in m):
            return ([m[reaminder],i])
            #print(m[reaminder])
        m[num]=i
        #print("------",reaminder)




num=[4,6,7,2,3]

print(targetSum(num))
o/p
[0, 1]

count the each number occurence in a give list

-------------------------------------------------------------------------------------------------------------------------------------
10.duplicate = [12,11,12,14,12,13,20,19,4,5,4,3,6,9]

{12: 4, 11: 1, 14: 2, 13: 1, 20: 1, 4: 2, 5: 1, 3: 1, 9: 1}

#print(set(duplicate))

dupl={}
for i in duplicate:
    if i in dupl:
        dupl[i] +=1
    else:
        dupl[i]=1

print(dupl)


--------------------------------------->weight of the give dicti<------------------------------------------
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
--------------------------------------------->sotred list based on string value<-------------------------------------------

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



