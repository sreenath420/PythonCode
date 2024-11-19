----------------------------------------------------------->Generator<--------------------------------------------------------
1.Python generators are easy way of creating iterators.it generates values one at a time from a given sequence insted of returning the entire sequence at once.
2.it is a special type of function which returns an iterator object.
3.in a generates function, a yield statement is used rather than a return statement.
4.The generator function cannot include the return keyword.if we include it then it will terminate the execution of the function.
5.The differnce between yield and return is that once yield returns a value the function is paused and the control is transferred to the caller local variables and thier states are remembered between successive calls. in case of the return statment value is retured and the exeuction of the function is terminated.
6.Methods like iter() and next() are implemented automatically in generator function.
7.Simple generators can be easily create using generator expressions. generator expressions create anonymous generate functions like lambda.
8.The syntax for generator expression is similar to that a list comprehension but the only differnce is square brackets are replaced with round parentheses. also list comprehension
produces the enitre list while the generator expression produces one item at a time which is more memory effcient than list comprehension.

Simple generator function that will generate numbers from 1 to 5

-------------->example-1<----------------------
def mygen():
    n=1
    yield n
    n +=1
    yield n
    n +=1
    yield n

mygen1=mygen()
print(next(mygen1))
print(next(mygen1))
print(next(mygen1))
print(next(mygen1))

1
2
note:-if you next(mygen1) it will iterator only one time it won't terminate the function untill execced the yield values
---------->example-2<------------------
--> generate example<--
def mygen():
        for i in range(1,20):
            yield i

num=list(mygen())
print(num)## Store all values generated by generator function in a list
output:-
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

-------->normal program<--------------------
for i in range(1,20):
    print(i)

ouput:-
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19


--------------------->Example-3<------------------------------------

def mygen():
    for i in range(1,20):
        if i%2==0:
            yield i

num=list(mygen())
print(num)

output:-
[2, 4, 6, 8, 10, 12, 14, 16, 18]

------------------->normal-program<---------------------------------------

for i in range(1,20):
    if i%2==0:
        print(i)

2
4
6
8
10
12
14
16
18


---------------->Example-4<-------------------------------------------

def myfib():
    num1,num2=0,1
    count=0
    while count <10:
        yield num1
        num1,num2=num2,num1+num2
        count+=1

fib=list(myfib())
print(fib)

output:-

[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


------------------------------------->Generator vs Normal Functions<-------------------------------


Generator is special function in python it gives sequence of items. 
