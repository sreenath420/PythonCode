-------------------------------------------------->Problem_1<-----------------------------------------------
line = "user=abc time=10"
# Expected output: {'user': 'abc', 'time': 10}

result = {}
for part in line.split():
    print(part)
    key, value = part.split('=')
    print(key, value)
    # Convert to int if it's numeric, else keep as string
    # result[key] = int(value) if value.isdigit() else value
    result[key]=value

print(result)

---------------------------------------------->Problem_2<---------------------------------------------------------

Given a list of file names, extract only .csv files using list comprehension.

result=[]
list=['file.txt','file2.csv','file3.csv']
for i in list:
    c=i.split('.')
    d=c[-1]
    if d=='csv':
        result.append(i)
print(result)

----------------------------------------------->Problem_3<---------------------------------------------------------------

data = [
    {"name": "Alice", "city": "Delhi", "age": 25},
    {"name": "Bob", "city": "Mumbai", "age": 30},
    {"name": "Charlie", "city": "Delhi", "age": 22},
    {"name": "David", "city": "Bangalore", "age": 28},
    {"name": "Eve", "city": "Mumbai", "age": 26}
]

result=sorted(data,key=lambda x:(x['city'],x['age']))

print(result)

