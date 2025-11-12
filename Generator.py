Here Question while preparing generators 
1.What is Generator
2.What is difference between Normal functions vs Generator
3.Drawback of Generator

----------------------------------------->1.What is Generator<-----------------------------------------

A Generator is special type of Iterator let allow you Iterator through sequence of values without stroing them all in memory at once

You create them using:
* Generator Functions(Using Yield)
* Generator Expressions(like list comprehensions but with())

2. Why Generators Exist
In normal functions or lists:
The entire list or result is created and stored in memory.
If you have a large dataset (say 1 TB), this will crash your program.
Generators solve this problem by producing one item at a time, only when needed.
Analogy:
Think of a generator as a “lazy waiter” — it prepares one dish (value) at a time only when the customer (your code) asks for it.
                                                                                                                        
                                                                                                                        
3. How a Generator Function Works

A normal function uses return → gives a result and exits.
A generator function uses yield → pauses the function, remembers its state, and can resume later.

Example:
def simple_gen():
    yield 1
    yield 2
    yield 3

gen = simple_gen()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
