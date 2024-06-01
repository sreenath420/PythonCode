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
{'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 2, 'f': 2, 'h': 1, 'g': 1}
