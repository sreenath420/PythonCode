What is Dictionary Comprehension?

A dictionary comprehension allows you to create a dictionary from an iterable (like a list, tuple, or another dictionary) in a single readable line.


Basic Syntax

{key_expression: value_expression for item in iterable if condition}

-------------------------->Program_1<-----------------------------

result={x:x**2 for x in range(1,6)}
print(result)

output:-
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


--------------------->Program_2<-------------------------------------------
result={x:x**2 for x in range(1,6) if x%2==0}
print(result)

ouput:-
{2: 4, 4: 16}

-------------------->Program_3<----------------------------------------
swap the values

data = {'a': 1, 'b': 2, 'c': 3}

result = {x:v for v,x in data.items() }

print(result)

output:-
{1: 'a', 2: 'b', 3: 'c'}

--------------->Program_4<-----------------

4️⃣ Example — Filter and Modify Existing Dictionary

Filter only those items whose value > 50.

marks = {'John': 85, 'Sara': 45, 'Mike': 60, 'Anna': 30}

result={k:v for k,v in marks.items() if v>50}
print(result) 

ouput:-

{'John': 85, 'Mike': 60}

------------------->Program_5<------------------------------

Convert names to uppercase and double the values.

students = {'john': 10, 'sara': 20, 'mike': 30}

result={k.upper():v*2 for k,v in students.items()}

print(result)

ouput

{'JOHN': 100, 'SARA': 400, 'MIKE': 900}

---------------->Program_6<---------------------

you want to make only the first letter uppercase for each key in the dictionary, not the whole word.

students = {'john': 10, 'sara': 20, 'mike': 30}

result={k.capitalize():v*2 for k,v in students.items()}

print(result)


{'John': 20, 'Sara': 40, 'Mike': 60}


----------------->Progarm_7<----------------------
result={x:{y:x*y for y in range(1,6)} for x in range(1,5)}

print(result)

output

{
  1: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5},
  2: {1: 2, 2: 4, 3: 6, 4: 8, 5: 10},
  3: {1: 3, 2: 6, 3: 9, 4: 12, 5: 15}
}


---------------->Program_8<---------------------

old = {'a': 10, 'b': 20, 'c': 30}
result={x:y+10 for x,y in old.items()}
print(result)

output:-

{'a': 20, 'b': 30, 'c': 40}

-------------->Program_9<------------------
Create a 3×3 matrix in dictionary form

matrix = {i: {j: i*j for j in range(1, 4)} for i in range(1, 4)}
print(matrix)
# Output:
# {1: {1: 1, 2: 2, 3: 3},
#  2: {1: 2, 2: 4, 3: 6},
#  3: {1: 3, 2: 6, 3: 9}}

------------->Program_10<---------------------

Convert list of tuples into dictionary

pairs = [("a", 1), ("b", 2), ("c", 3)]
result={x:y for x,y in pairs}
print(result)
output:-
{'a': 1, 'b': 2, 'c': 3}


----------->Program_11<----------------------

Map numbers to “Even” or “Odd”:

result={x:("even" if x%2==0 else "Odd") for x in range(1,10)}
print(result)

ouput
{1: 'Odd', 2: 'even', 3: 'Odd', 4: 'even', 5: 'Odd', 6: 'even', 7: 'Odd', 8: 'even', 9: 'Odd'}

------------->Program_11<------------------

input =['apple', 'banana', 'kiwi']
#Expected output: {'apple': 5, 'banana': 6, 'kiwi': 4}
result={x:len(x) for x in input}
print(result)

Normal for loop 

dict={}
for i in input:
    dict[i]=len(i)

print(dict)


