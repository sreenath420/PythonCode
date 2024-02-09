for i in range(1,5):-->1,2,3,4
    for j in range(1,i+1):1,2
        print(j,end=' ')
    print(' ')
    
    
 
 
step -1   i:-- range(1,5)--->1,2,3,4
          here i value is 1
          j:-- range(1,2)-->1
          print(j) -->1
      
step -2  here i value is 2
         j:-- range(1,3)-->1,2
         print(j) 1 2
step -3  here i value is 3
         j:-- range(1,4) -->1,2,3
         print(j)1 2 3
step -4  here i value is 4
         j: range(1,5)1,2,3,4
         print(j)1 2 3 4
         
 1
 1 2
 1 2 3
 1 2 3  4
 
 
 or i in range(1,5):
    for j in range(1,i+1):
        print('*',end=' ')

    print( )


*
* *
* * * 
* * * *