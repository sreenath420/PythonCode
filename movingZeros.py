def moveZeros(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i]!=0:
            nums[j]=nums[i]
            j +=1

    for k in range(j,len(nums)):
        nums[k]=0
    return nums


num=[6,7,0,9,0,3,3,4,5,0]

print(moveZeros(num))

New_list= [num for num list if list!=0]
New= [num for num list if list=0]
Print(new_list+ New)
