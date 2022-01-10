from math import factorial
def fact():
    return 1 if (n==0 or n==1) else n * factorial(n-1)
n = int(input("Enter your number: "))
print("factorial of ",n,"is", factorial(n))