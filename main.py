# Part 1
def SumN(Num):
    Sum = 0
    for i in range(1, Num+1):
        Sum += i
    return Sum

def SumN3(Num):
    Sum3 = 0
    for i in range(1, Num+1):
        Sum3 += i**3
    return Sum3


Num = int(input("Please enter the natural number: "))
print("The sum of natural numbers:", SumN(Num))
print("The sum of the cubs of natural numbers:", SumN3(Num))
print(" ")

# Part 2

Value = int(input("Please enter the number of Fibonacci element: "))

def Fibonacci(a):
    if a < 0:
        return "Error"
    elif a <= 1:
        return a
    else:
        return Fibonacci(a - 1) + Fibonacci(a - 2)


print("The", Value, "-th of Fibonacci element is:", Fibonacci(Value))
print(" ")

# Part 3

N = int(input("Please enter the number: "))

def Factorial(b):
    if b <= 1:
        return 1
    else:
        return b * Factorial(b - 1)


print("The factorial of the number is:", Factorial(N))
print(" ")