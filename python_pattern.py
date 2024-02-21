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
--------------------------------------------------------Program-5 ----------------------------------------------------------------------------------------

1 1 1 1 1  
2 2 2 2  
3 3 3  
4 4  
5 

u=0
for i in range(5,0,-1): #11 8 5
    u +=1
    #print(u)
    for j in range(1,i+1):
        print(u,end=' ')
    print(' ')



step :-1 i in range(5,0,-1) ----> 5
          u  +=1 --> u is 1 here
         j in range(1,6) -->(1,2,3,4,5)
           print(u,end=' ') --> 1 1 1 1 1
          
 
step :-2 i in range(5,0,-1) ----> 4
          u  +=1 --> u is 2 here
         j in range(1,5) -->(1,2,3,4)
           print(u,end=' ') --> 2 2 2 2
           
step :-3 i in range(5,0,-1) ----> 3
          u  +=1 --> u is 3 here
         j in range(1,4) -->(1,2,3)
           print(u,end=' ') --> 3 3 3
           
step :-4 i in range(5,0,-1) ----> 2
          u  +=1 --> u is 2 here
         j in range(1,3) -->(1,2)
           print(u,end=' ') --> 4 4
step :-5 i in range(5,0,-1) ----> 1
          u  +=1 --> u is 1 here
         j in range(1,2) -->(1)
           print(u,end=' ') --> 5

------------------------------------------Program 6------------------------------
0 1 2 3 4 5 
0 1 2 3 4 
0 1 2 3 
0 1 2 
0 1

for i in range(5,-1):
    #Print(i)
    for j in range(0,i+1):
	    print(j,end=' ')
    print(' ')
		
		0,1,2,3,4,5
		
step 1 --> i:-- range(0,6)-10,1,2,3,4,5
            here j value is 0,1
          print(j)-->0
      
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
------------------------------------------Program 7------------------------------
* * * *
* * * *
* * * *
* * * *



for i in range(1,5):
    for j in range(1,5):
        print('*',end=' ')
    print(' ')
        
		
		

step:1 i value is 1,
       j value is 1,2,3,4
       * print 4 times here * * * *
 
step:2 i value is 2,
       j value is 1,2,3,4
       * print 4 times here * * * *
       
step:3 i value is 3,
       j value is 1,2,3,4
       * print 4 times here * * * *
       
step:4  i value is 4,
       j value is 1,2,3,4
       * print 4 times here * * * *


------------------------------------------Program 8------------------------------
5 5 5 5 5 
5 5 5 5 
5 5 5 
5 5 
5

for i in range(6,1,-1):
    for j in range(1,i):
	    print(5,end=" ")
    print(' ')
------------------------------------------Program 9------------------------------
1 
2 1 
3 2 1 
4 3 2 1 
5 4 3 2 1

for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print(' ')	
	
step 1 --> i:-- range(1,6)-1,2,3,4,5
            here j value is 1
          print(j)-->1
      
step -2  here i value is 2
         j:-- range(2,0)-->2,1
         print(j) 2 1
step -3  here i value is 3
         j:-- range(3,0) -->3,2,1
         print(j)3 2 1
step -4  here i value is 4
         j: range(4,0) 4,3,2,1
         print(j) 4 3 2 1 
step -5  here i value is 5
         j: range(5,0) 5,4,3,2,1
         print(j) 5 4 3 2 1
------------------------------------------Program 10------------------------------

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1


for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
	
	
step 1 --> i:-- range(5,0)-5,4,3,2,1
            here j value is 5
          print(j)-->5 4 3 2 1
      
step -2  here i value is 4
         j:-- range(4,0)-->4,3,2,1
         print(j) -->4 3 2 1 
step -3  here i value is 3
         j:-- range(3,0) -->3,2,1
         print(j)3 2 1
step -4  here i value is 2
         j: range(2,0) 2,1
         print(j) 2 1 
step -5  here i value is 1
         j: range(1,0) 1
         print(j) 1
