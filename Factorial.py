#Karen Byrne 29/03/2018
#Exercise 6 Factorial

def factorial(x):
    factx = x 
    for i in range (1,x+1):
        factx = factx * (factx-1)
    return factx

print("The factorial of 10 is",factorial(10))
