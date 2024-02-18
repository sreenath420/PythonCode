def reverse(s):
    str=' '
    for i in s:
        str=i+str
    return str


s='Sreenath'
print(reverse(s))


8
12
16
20
24
28

def print_sequence():
    for i in range(8, 29, 4):
        print(i)
