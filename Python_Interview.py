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







