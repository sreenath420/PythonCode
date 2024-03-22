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
 3 3 3
 4 4 4 4 4 
 5 5 5 5 5 5
		 
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


------------------------------------------------Program 11--------------------------------------------------------------


step:-1 i in range(1,8) ---->print(i) 1
        j in range(0,1) -->0
        print(1*0) --->0
        
 0
 
 
 step:-2 i in range(1,8) ---->print(i) 2 
        j in range(0,2) -->0 1
        print(1*0) --->0 #print(1*2) --->2
        
 
 0 2
 
 
  step:-3 i in range(1,8) ---->print(i) 3 
        j in range(0,3) -->0 1 2
        print(3*0) --->0 #print(3*1) --->3 #print(3*2)---->6
        
 
 0 3 6
 
 step:-4 i in range(1,8) ---->print(i) 4
        j in range(0,4) -->0 1 2 3
        print(4*0) --->0 #print(4*1) --->4 #print(4*2)---->8 #print(4*3)--->12
        
 0 4 8 12
 
 
 step:-5 i in range(1,8) ---->print(i) 5
        j in range(0,5) -->0 1 2 3 4
        print(5*0) --->0 #print(5*1) --->5 #print(5*2)---->10 #print(5*3)--->15 #print(5*4)  -->20
 0 5 10 15 20
 
 step:-6 i in range(1,8) ---->print(i) 6
        j in range(0,6) -->0 1 2 3 4 5
        print(6*0) --->0 #print(6*1) --->6 #print(6*2)---->12 #print(6*3)--->18 #print(6*4)  -->24 #print(6*5)  -->30 #print(6*6)  -->36
 0 6 12 18 24 30 36
 
 step:-6 i in range(1,8) ---->print(i) 7
        j in range(0,7) -->0 1 2 3 4 5 6
        print(7*0) --->7 #print(7*1) --->7 #print(7*2)---->14 #print(7*3)--->21 #print(7*4)  -->28 #print(7*5)  -->35 #print(7*6)  -->42 print(7*7) --->49
 0 7 14 21 28 35 42 49


------------------------------------------------program 12-------------------------------------------------

A 
B C 
D E F 
G H I J 
K L M N O



num=65  -->A

for i in range(6):
    for j in range(i): 
        ch=chr(num)
        #ch +=1
        print(ch,end=' ')
        num +=1
    print(' ')


step:1 ----> i in range(6) -->0
        for j in ragne(0) 
        ch=chr(num)==> 65
        print(ch,end=' ') A
        num +=1 ---> 66
        

step:2 ----> i in range(6) -->1
        for j in ragne(1) -->1
        ch=chr(num)==> 66
        print(ch,end=' ') A B
        num +=1 ---> 67
        
step:3 ----> i in range(6) -->2
        for j in ragne(2) -->0 1
        ch=chr(num)==> 67
        print(ch,end=' ') D E F
        num +=1 ---> 67
        
        
step:3 ----> i in range(6) -->3
        for j in ragne(3) -->0 1 2 
        ch=chr(num)==> 68
        print(ch,end=' ') G H I J
        num +=1 ---> 69
        
        
step:4 ----> i in range(6) -->4
        for j in ragne(3) -->0 1 2 3
        ch=chr(num)==> 69
        print(ch,end=' ') K L M N O
        num +=1 ---> 70



---------------------------------------program 13--------------------------------------------------

A 
B B 
C C C 
D D D D 
E E E E E


for i in range(64,70):
    for j in range(64,i):
	    print(chr(i),end=' ')
    print(' ')
    
    
    
step:1 ----> i in range(65,70)
              print(65)
           for j in range(64,i) -->64
            print(chr(i),end=' ') 
           A
        
step:2 ----> i in range(65,70)
              print(66)
           for j in range(64,i) -->64 65
            print(chr(i),end=' ') 
           B B
           
        
step:3 ----> i in range(65,70)
              print(67)
           for j in range(64,i) -->64 65 66
            print(chr(i),end=' ') 
           C C C
        
step:4 ----> i in range(65,70)
              print(68)
           for j in range(64,i) -->64 65 66 67
            print(chr(i),end=' ') 
           D D D D
        
        
step:5 ----> i in range(65,70)
              print(69)
           for j in range(64,i) -->64 65 66 67 68 69 
            print(chr(i),end=' ') 
           E E E E E
      

---------------------------------------program 14--------------------------------------------------
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64


   
   
for i in range(1,9):
    for j in range(1,i+1):
        print(i*j,end=' ')
    print('\n')   
    
 
step-1: i =1
        j here is range(1,2)-->1
        print(i*j)--> 1*1  1
        
     1
     

step-2: i =2
        j here is range(1,3)-->1 2
        print(i*j)--> 1*2 & 2*2 
      2 4
      
step-3: i =3
        j here is range(1,4)-->1 2 3
        print(i*j)--> 1*3 & 2*3 & 3*3
        3 6 9
        
step-4: i =4
        j here is range(1,5)-->1 2 3 4
        print(i*j)--> 1*4 & 2*4 & 3*4 & 4*4
        4 8 12 16
        
step-5: i =5
        j here is range(1,6)-->1 2 3 4 5
        print(i*j)--> 1*5 & 2*5 & 3*5 & 4*5 & 5*5
        5 10 15 20 25 
     
step-6: i =6
        j here is range(1,7)-->1 2 3 4 5 6
        print(i*j)--> 1*6 & 2*6 & 3*6 & 4*6 & 5*5 & 5*6
        6 12 18 24 30 36
        
step-7: i =7
        j here is range(1,7)-->1 2 3 4 5 6 7
        print(i*j)--> 1*7 & 2*7 & 3*7 & 4*7 & 5*7 & 6*7 & 7*7
        7 14 21 28 35 42 49
        
step-8: i =8
        j here is range(1,7)-->1 2 3 4 5 6 7 8
        print(i*j)--> 1*8 & 2*8 & 3*8 & 4*8 & 5*8 & 6*8 & 7*8 & 8*8
        8 16 24 36 44 50 58 64
---------------------------------------program 15--------------------------------------------------
1 2 3 4
1 2 3 4
1 2 3 4
1 2 3 4


for i in range(1,5):
    for j in range(1,5):
        print(j,end=' ')
    print(' ')
    
step-1:- i =1
       j here range(1,5)
       print(j) 1 2 3 4
step-2:- i =2
       j here range(1,5)
       print(j) 1 2 3 
       
step-3:- i =3
       j here range(1,5)
       print(j) 1 2 3 4
       
step-4:- i =4
       j here range(1,5)
       print(j) 1 2 3 4
---------------------------------------program 16--------------------------------------------------
* * * * *
* * * *
* * *
* *
*

for i in range(6,0,-1):
    for j in range(i):
        print('*',end=' ')
    print(' ')
    
step-1: i=6
       j here range(i) ---->6 means * * * * * *
       print('*'end=' ')
     * * * * * *
     
     
step-2: i=5
       j here range(i) ---->5 means * * * * * 
       print('*'end=' ')
     * * * * * 
     
step-3: i=4
       j here range(i) ---->5 means * * * * 
       print('*'end=' ')
     * * * * 
     
step-4: i=3
       j here range(i) ---->5 means * * * 
       print('*'end=' ')
     * * * 
     
step-5: i=2
       j here range(i) ---->5 means * * 
       print('*'end=' ')
     * * 

step-5: i=1
       j here range(i) ---->5 means *  
       print('*'end=' ')
     * 

---------------------------------------program 17--------------------------------------------------

* * * * *
*       *
*       *
*       *
*       *
* * * * *
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==6-1 or j==1 or j==6-1: 
            print('*',end='')
        else:
            print(' ',end='')
    print()
	
	
	

step 1:- i range(1,6): i------->1
         j range(1,6): j-------> 1,2,3,4,5
		 if i==1 or i==6-1 or j==1 or j==6-1:
          here i is 1 so we are getting * * * * and j==1 we are getting *
		  it will be print this line 
		  * * * * *
		  
step 2:- i range(1,6): i------->2
         j range(1,6): j-------> 1,2,3,4,5
		 if i==1 or i==6-1 or j==1 or j==6-1:
		 here i is 2 so we are getting  and j==1 and j==5 we are getting *
		 it will be print this line
		 *       *
step 3:- i range(1,6): i------->3
         j range(1,6): j-------> 1,2,3,4,5
		 if i==1 or i==6-1 or j==1 or j==6-1:
		 here i is 3 so we are getting  and j==1 and j==5 we are getting *
		 it will be print this line
		 *       *
step 4:- i range(1,6): i------->4
         j range(1,6): j-------> 1,2,3,4,5
		 if i==1 or i==6-1 or j==1 or j==6-1:
		 here i is 4 so we are getting  and j==1 and j==5 we are getting *
		 it will be print this line
		 *       *
		 
step 5:- i range(1,6): i------->5
         j range(1,6): j-------> 1,2,3,4,5
		 if i==1 or i==6-1 or j==1 or j==6-1:
		 here i is 5 so we are getting  and j==1 and j==5 we are getting *
		 it will be print this line
		 * * * * *

   ------------------------------------------Program 18------------------------------------------------------------------------------------
               1
	    1  2
        1  2   3
      1 2  3   4
    1 2 3  4   5
 
 
 
 
 for i in range(1,6):
    u = 1

    for j in range(6,0,-1):

        if j>i:
            print(' ',end=' ')
        else:
            print(u,end=' ')
            u +=1
    print(' ')
    
  
  
step:-1 i is here 1 
   u =1
   j here range(6,0,-1) 6 5 4 3 2 1
   a)6>1(j>i)---->here j>i is true so one space print
   b)5>1(j>i)---->here j>i is true so one space print
   c)4>1(j>i)---->here j>i is true so one space print
   d)3>1(j>i)---->here j>i is true so one space print
   e)2>1(j>i)---->here j>i is true so one space print
   f)1>1 is false so else statement going to print here so we can u value inside the else stament that is going to be 1 after 5 blank spaces
                             1
   

 step:-2 i is here 2
   u =1
   j here range(6,0,-1) 5 4 3 2 1
   a)5>2(j>i)---->here j>i is true so one space print
   b)4>2(j>i)---->here j>i is true so one space print
   c)3>2(j>i)---->here j>i is true so one space print
   d)2>2(j>i)---->here is false so else statment going to print is u=1 so print u one after 4 space 1  
   e)1>2(j>i)---->here is false so else stament going to print inside else u have given value u +=1 so u value going to be 2
                        1 2
step:-3 i is here 3
   u =1
   j here range(6,0,-1)  4 3 2 1
   a)4>3(j>i)---->here j>i is true so one space print
   b)3>3(j>i)---->here j>i false so else statement going to print is u=1 so print u one after 3 space 1 
   c)2>3(j>i)---->here j>i false so else stament going to print inside else u have given value u +=1 so u value going to be 2
   d)1>3(j>i)---->here j>i false so else stament going to print inside else u have given value u +=1 so u value going to be 3
   
                      1 2 3
step:-4 i is here 4
   u =1
   j here range(6,0,-1)  3 2 1
   a)4>4(j>i)---->here j>i false so else statement going to print is u=1 so print u one after 3 space 1
   b)3>3(j>i)---->here j>i false so else stament going to print inside else u have given value u +=1 so u value going to be 2
   c)2>3(j>i)---->here j>i false so else stament going to print inside else u have given value u +=1 so u value going to be 3
   d)1>3(j>i)---->here j>i false so else stament going to print inside else u have given value u +=1 so u value going to be 4
   
                      1 2 3 4
   
 ----------------------------------------- program 19 ------------------------------------------------  

    *     
  *   *   
 *     * 
  *   *   
    *     
for i in range(5):
    for j in range(5):
        if  i+j ==2 or i-j==2 or i +j==6 or j-i==2:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

-------------------------------------------------program 20 -----------------------------------------------------------------------------

1  
1 1  
1 2 1  
1 3 3 1  
1 4 6 4 1 

for i in range(5):
    num=1
    for j in range(1,i+2):
        print(num,end=" ")
        num=num*(i+1-j)//j
    print(' ')




for i in range(5) : This loop iterates over each row of the pattern.it goes from 0 to rows -1
num =i: initalize the variable num to 1 for each row. This variable will hold the numbers to be printed on each row.
for j in range(1,i+2): this loop iterates over each column in the current row.it goes from 1 to i+1
print(num,end=" ") prints the value of num without a newline character this ensure that all numbers in the same row are printed on the same line
num = num*(i+j-j)//j: this line updates the value of num for the next column it calcuates the next number in the row based on the previous number using the formula (i+1-)//j this 
formula generates pascals triangle pattern.



-----------------------------------------------------program 21----------------------------------------------------------------------------------

0 
1 *
2 **
3 ***
4 ****
5 *****


for i in range(6):
    print(i,"*"*i)


--------------------------------------------------->program 22<------------------------------------------------------------------------------


      *       
        *     
          *   
* * * * * * * 
          *   
        *     
      *   

for i in range(0,7):
    for j in range(0,7):
        if i==3 or j-i==3 or i+j==9:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


-------------------------------------------------->program 23<----------------------------------------------------------------------------------

E D C B A 
 D C B A 
  C B A 
   B A 
    A 

for i in range(5):
    for j in range(i):
        print(" ",end="")
    for k in range(5-i):
        print(chr(69-i-k),end=' ')
    print()
