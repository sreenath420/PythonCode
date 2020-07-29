def reverse(s):
    str=' '
    for i in s:
        str=i+str
    return str


s='Sreenath'
print(reverse(s))