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
