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



--------------------------------------------------------->Fib number<-----------------------------------------------------------------------

try:

    n = int(input("Enter a Number"))
    a = 0
    b = 1

    if n == 0:
        print("not egligble for fib number")
    elif n == 1:
        print("Fib number is", b)

    else:
        count = 0
        while count < n:
            print(a)
            n1 = a + b
            a = b
            b = n1
            # n = a + b]
            count +=1
except ValueError:
    print("Enter the valid number")


