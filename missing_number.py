Find Missing numbers in give list
Input:
List=[2,5,7,9]
Output:
List=[3,4,6,8]

range(list[0],list[-1])
range(2,9)
2,3,4,5,6,7,8
if not in List


def miss_number(nums):
    result=[]
    for i in range(nums[0],nums[-1]):
        #print(i)
        if i not in nums:
            result.append(i)

    return result

nums=[2,5,7,9]
print(miss_number(nums))