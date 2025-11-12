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

🧠 Explanation:

Each yield temporarily pauses the function and returns a value.

The function resumes from where it left off on the next call.

When there are no more yields, it raises StopIteration.

🧮 4. Generator vs Normal Function
Feature	Normal Function	Generator Function
Uses	return	yield
Returns	Single value	Iterator (sequence of values)
Memory	Loads all at once	One item at a time
Execution	Ends after return	Pauses and resumes
Example use	Simple computation	Stream of data, large datasets
🧠 5. Generator Example: Range-like Function

Here’s how Python’s range() internally works (simplified):

def my_range(n):
    i = 0
    while i < n:
        yield i
        i += 1


Now:

for num in my_range(5):
    print(num)


✅ Output:

0
1
2
3
4


✅ Memory benefit:
Even if you call my_range(1_000_000_000), it doesn’t create a billion items in memory — it produces them one by one.

🧩 6. Generator Expression (One-Liner Form)

You can create a generator without yield, just like a list comprehension but with parentheses ().

Example:
squares = (x*x for x in range(5))
print(next(squares))  # 0
print(next(squares))  # 1
print(next(squares))  # 4


✅ Generator expressions are memory-efficient and fast for streaming data.

⚙️ 7. Real-World Use Cases (Interview-Level)
Use Case	Example
Reading large files	Read line by line instead of loading full file
Data pipelines / ETL	Stream rows between stages without intermediate lists
Infinite sequences	Generate endless numbers (e.g., Fibonacci, primes)
API pagination	Fetch next page only when needed
Lazy evaluation	Don’t compute until requested
Example: Reading a Big File
def read_large_file(file_path):
    with open(file_path) as f:
        for line in f:
            yield line.strip()


Use:

for line in read_large_file("bigdata.txt"):
    process(line)


✅ Reads file one line at a time, not all at once.

🔍 8. How yield Works Internally (Key Interview Insight)

When a function has yield:

Calling it does not execute the function immediately.
It returns a generator object.

Each time you call next(), the function runs until it hits yield, returns that value, and pauses.

When function ends → raises StopIteration.

🧠 9. Common Interview Questions (with Answers)
Q1: What’s the difference between an iterator and a generator?

Answer:

An iterator is any object with __iter__() and __next__() methods.

A generator automatically creates an iterator for you when you use yield.

Q2: What’s the benefit of a generator over a list?

Answer:

Lists store all values in memory.

Generators yield one value at a time → memory efficient for large or infinite data streams.

Q3: Can a generator be reused?

Answer: ❌ No.
Once a generator is exhausted, you can’t reuse it. You must create it again.

Q4: What happens when you call next() on an exhausted generator?

Answer:
Raises StopIteration exception.

Q5: How do you convert a generator into a list?
list(gen)


⚠️ But be careful — this will consume all items into memory.

🧩 10. Advanced Example — Fibonacci Generator
def fib_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


Use:

gen = fib_gen()
for _ in range(10):
    print(next(gen))


✅ Generates infinite Fibonacci numbers without ever storing them all.

💡 Bonus Tip (Interview Pro-level)

When an interviewer asks:

“How would you process a 10 GB log file in Python efficiently?”

Answer confidently:

“I’d use a generator function that reads one line at a time, yielding each record for processing. This prevents loading the full file into memory, improving performance and scalability.”

🔥 That’s the kind of answer that gets you shortlisted.
