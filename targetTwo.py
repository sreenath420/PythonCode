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

print(targetSum((num)))
