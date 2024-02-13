------------------------------------------Program 1------------------------------
output-
1
1 2
1 2 3
1 2 3 4    

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
         
------------------------------------------Program 2------------------------------ 
output-
*
* *
* * * 
* * * *
 
 for i in range(1,5):
    for j in range(1,i+1):
        print('*',end=' ')

    print( )

------------------------------------------Program 3------------------------------
o/p-
 1
 2 2
 2 2 2
 3 3 3 3
 4 4 4 4 4 
		 
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=' ')
    print(' ') 
        
step -1   i:-- range(1,5)--->1,2,3,4
          here i value is 1
          j:-- range(1,2)-->1
          print(i) -->1
      
step -2  here i value is 2
         j:-- range(1,3)-->1,2
         print(i) 2 2
         
step -3  here i value is 3
         j:-- range(1,4) -->1,2,3
         print(i)3 3 3
         
step -4  here i value is 4
         j: range(1,5)1,2,3,4
         print(i)4 4 4 4
        
------------------------------------------Program 4------------------------------
o/p-  
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1 

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(i,end=' ')
    print( )  

step 1 --> i:-- range(5,0,-1)--->5,4,3,2,1
            here j value is 1,2,3,4,5
          print(i) -->5 5 5 5 5
      
step -2  here i value is 4
         j:-- range(1,5)-->1,2,3,4
         print(i) 4 4 4 4
step -3  here i value is 3
         j:-- range(1,4) -->1,2,3
         print(i)3 3 3
step -4  here i value is 2
         j: range(1,3) 1,2
         print(i) 2 2
step -5  here i value is 1
         j: range(1,1) 1
         print(i) 1               
 
  
