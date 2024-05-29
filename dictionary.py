------------------------------------------------------------------->Dictionaries in Python<------------------------------------------------------------------
A Python dictionary is a data structure that stores the value in key:value pairs.

Example:

As you can see from the example, data is stored in key:value pairs in dictionaries, which makes it easier to find values.

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
print(Dict)

syntax
dict_var = {key1 : value1, key2 : value2, …..}



n Python, a dictionary can be created by placing a sequence of elements within curly {} braces, separated by a ‘comma’.

The dictionary holds pairs of values, one being the Key and the other corresponding pair element being its Key:value.

Values in a dictionary can be of any data type and can be duplicated, whereas keys can’t be repeated and must be immutable. 

Note – Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly. 

Note example code below


Dict = {'cat': 'Ujjwala', 'Cat': 'SreeNath', 3: 'SreeNath'}
print(Dict)
o/p
{'cat': 'Ujjwala', 'Cat': 'SreeNath', 3: 'SreeNath'}


Dict = {'Name': 'Ujjwala', 1: [1, 2, 3,[4,5,6],7,8,9,10]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict[1][3])

o/p

[4, 5, 6]



Different Ways to Create a Python Dictionary

Dict = {} 
print("Empty Dictionary: ") 
print(Dict) 
  
Dict = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'}) 
print("\nDictionary with the use of dict(): ") 
print(Dict) 
  
Dict = dict([(1, 'Geeks'), (2, 'For')]) 
print("\nDictionary with each item as a pair: ") 
print(Dict) 


o/p
Empty Dictionary: 
{}

Dictionary with the use of dict(): 
{1: 'SreeNath', 2: 'Ujjwala', 3: 'Friends'}

Dictionary with each item as a pair: 
{1: 'SreeNath', 2: 'Ujjwala'}


Nested Dictionray

Dict = {1: 'SreeNath', 2: 'Ujjwala',
        3: {'A': 'Welcome', 'B': 'To', 4:{'C': 'Ujjwala'}}}

print(Dict[3][4]['C'])


how to get ouput
Sree jwala
print(Dict[1][0:4],Dict[2][2:])

How to get output

{'D': 1}

Dict = {1: 'SreeNath', 2: 'Ujjwala',
        3: {'A': 'Welcome', 'B': 'To', 4:{'C': ['Ujjwala','SreeNath','Sree'],5:{'D':1}}}}

print(Dict[3][4][5])


how to access the dict values
example
method1:
print(Dict[2])
method2
print(Dict.get(2))

How to delete the dict values
by using del function we can deleted
below example how to delete nested dictionaries
Dict = {1: 'Geeks', 'name': 'For', 3: 'Geeks',4:{'A':'SreeNath','B':'Ujjwala'}}

#print("Accessing a element using get:")
#print(Dict.get('name'))

del(Dict[4]['B'])
print(Dict)
	

dict2 = {1:{  # outer dictionary
    'Name': 'Steve',
    'Age': 30,
    'Designation': 'Programmer',
    'address': {  # inner dictionary
           'Street': 'Brigade Road',
           'City': 'Bangalore',
           'Country': 'India'
    }
}}

#print(dict2[1]['address']['City'])

print((dict2[1].values()))


o/p
dict_values(['Steve', 30, 'Programmer', {'Street': 'Brigade Road', 'City': 'Bangalore', 'Country': 'India'}])



by appying for loop
if you mention dictiory items it will give both key and value other wise it will pring only the keys


dict2 ={
       'Name':
           {
               'first_name':'Steve',
               'Last_name':'Jobs'
           },
       'Age':30,
       'Designation':'Programmer',
       'address':
           {
           'Street':'Rockins Road',
           'City':'Bangalore',
           'Country':'India'
           }
      }

for k,v in dict2.items():
        print(v)
---------------------------------minimum value of the in the given dict----------------------------------------------


dict={"a":4,"b":3,"c":7}
y=min(dict.values())
print(y)
o/p
3


-------------------------------->GET THE VALUES FROM YOU THE PARTICAL RANGE OF KEY<--------------------------

Input={"Gfg" : 6, "is" : 7,"best" : 9, "for" :8,"hours" :11}
i, j = 9, 12

print(Input)

res=dict()
for k,v in Input.items():
    if v>=i and v<j:
        res[k]=v

print(res)
o/p
{'best': 9, 'hours': 11}

----------------------------------->GET THE VALUE FROM BELOW VALUE<-------------------------------------------------------------
nested_dict = {'a': {'b': {'c': 42}}}
keys = ['a', 'b', 'c']
output:-42
def get_nested_values(nested_dict,keys):
    for i in keys:
        nested_dict=nested_dict[i]
        #print(nested_dict)
    return nested_dict

print(get_nested_values(nested_dict,keys))
