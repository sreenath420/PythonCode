Python practise


--------------------------------------------------------------------------->Dictionaries<----------------------------------------
1.What is a Dictionary in Python?

A dictionary is a collection of key–value pairs — just like a real dictionary where a word (key) has a meaning

2.Why Dictionaries Are So Useful (Main Reasons)?

Fast Lookups (O(1) Time Complexity)

Dictionaries are implemented using hash tables internally.

This means lookup, insert, and delete operations happen almost instantly (constant time).

Example:-

employees = {"E101": "Alice", "E102": "Bob"}
print(employees["E101"])  # Instant lookup — no loop needed


                                                    ------>Program1<--------

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Delhi']
# Expected output → {'name': 'Alice', 'age': 25, 'city': 'Delhi'}

solution:
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'Delhi']

c=dict(zip(keys,values))
print(c)


                                                 ---------->Program2<----------------------
data = {'name': 'Alice', 'age': 25, 'city': 'Delhi'}
print(data["city"])


                                                ---------->Program3<------------------------
data1 = {'name': 'Alice', 'age': 25, 'city': 'Delhi'}
data2 ={'village': 'praveen', 'num': 25, 'heigh': 'chennai'}

data = {**data1, **data2}
print(data)

Note: if there are duplicate key it will merge else it will append

                                              ----------->Program4<--------------------------
scores = {'Alice': 90, 'Bob': 75, 'Charlie': 92}
# Expected output: Charlie (max)

Solutions

topper = max(scores.items(), key=lambda x: x[1])
print(topper)


scores = {'Alice': 90, 'Bob': 75, 'Charlie': 92, 'dav': 20}
print(max(scores, key=scores.get))



print(scores.items())
c=max(scores.items(),key=lambda x: x[1])
print(c)


max_score = 0
topper = ' '

for name, score in scores.items():
    if score > max_score:
        max_score = score
        topper = name

print(topper)


                                                ---------->Program5<--------------------

items = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
# Output: {'apple': 3, 'banana': 2, 'orange': 1}
dict={}
for i in items:
    if i in dict:
        dict[i]+=1
    else:
        dict[i]=1
print(dict)


✅ 2️⃣ Using dict.get() (shorter loop)
counts = {}

for item in items:
    counts[item] = counts.get(item, 0) + 1

print(counts)

Explanation : get function returns values of the key mentioned if there is no key then returns defaults value 
Output:
{'apple': 3, 'banana': 2, 'orange': 1}

🔍 Explanation
counts.get(item, 0) returns the current count if it exists, or 0 otherwise.


Then we add 1 and assign it back.



✅ 3️⃣ Using collections.Counter (one-liner)
from collections import Counter
counts = Counter(items)
print(dict(counts))

Output:
{'apple': 3, 'banana': 2, 'orange': 1}

✅ Best for production code — short and optimized.



Problem 6:
Solution1:

data = {'a': 1, 'b': 2, 'c': 3}

{1: 'a', 2: 'b', 3: 'c'}

reversed={v:k for k,v in data.items()}
print(reversed)

Solution 2:
data = {'a': 1, 'b': 2, 'c': 3}

reversed_dict = {}

for key, value in data.items():
    reversed_dict[value] = key

print(reversed_dict)

Problem 7
data = {'Alice': 45, 'Bob': 75, 'Charlie': 60, 'David': 30}

# Filter values greater than 50

fiilter={k:v for k,v in data.items() if v>50}
print(fiilter)

Solution 2 🎉
dict={}
for key,value in data.items():
    if value>50:
        dict[key]=value
        
print(dict)











