----------------------------------------------------------> factorial Number <--------------------------------------------------

try:
    num = int(input('Enter Number\t'))
    factorial = 1
    if num == 0:
        print("o/p is 1")
    elif num < 0:
        print("not exist")
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print(factorial)

except ValueError:
    print("Error:Please enter a Valid Number")
