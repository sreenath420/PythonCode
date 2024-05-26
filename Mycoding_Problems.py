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
