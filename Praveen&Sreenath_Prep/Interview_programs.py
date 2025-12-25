LIST
-------------------------------------->1.Program<----------------------------
Remove Dupliactes in given list
list=[1,2,4,4,5,6,6,7,7]

Method:-1
print(set(list))

Method:-2
list2=[]
for i in list:
    if i not in list2:
        list2.append(i)
print(list2)

Ouput:-
[1, 2, 4, 5, 6, 7]
------------------------------------------>2.Program<------------------------------------
write python program to get repeted value which value repeatec 3 times here
comm_value =[2, 6]

li=[1,2,3,4,6,7,8,9,9,0,8,0,2,2,6,6,87,65,34,23]

result={}
for i in li:
    if i in result:
        result[i] +=1
    else:
        result[i] =1
print(result)

re=[x for x,v in result.items() if v==3]
print(re)

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Dictionary
--------------------------------------------->1.Program<---------------------------------
Write a python function dict_sort_by_value(dict) so that for given dictionary, it will return the dictionary with sort by value

sorted(iterable, key=None, reverse=False)
Key: key parameter decides the on which the iterable should sorted 

dict1 = {1001:'A', 1002:'B', 1003:'A', 1004:'C',  1005:'B',   1006:'C'}
output: {1001:'A', 1003:'A', 1002:'B', 1005:'B', 1004:'C', 1006:'C'}



dict2=dict(sorted(dict1.items(), key=lambda x:x[1]))
print(dict2)


---------------------------------------->2.Program<------------------------------------------
Sort the following list of players based on their reward in descending order (highest reward first) without using pandas.

  revrese=True Means it gives values descending if you don't mention 'True' by default it gives ascending order

players = [
    {'Name': 'Alan Turing', 'age': 25, 'reward': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'reward': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'reward': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'reward': 15000},
]


val=sorted(players,key=lambda x:(x['reward']),reverse=True)
print(val)


Output:-

[{'Name': 'Mikhail Tal', 'age': 40, 'reward': 15000}, {'Name': 'Alan Turing', 'age': 25, 'reward': 10000}, {'Name': 'Sharon Lin', 'age': 30, 'reward': 8000}, {'Name': 'John Hopkins', 'age': 18, 'reward': 1000}]
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
STRING
---------------------------------------->1.Program<------------------------------------------------

s= "DataEngineering"

#Q1. Reverse the string using a single line command; hint - via slicing


#Q2. Reverse the string without using single line command; hint - via a loop

result=''
for i in s:
  result =i + result
print(result)
