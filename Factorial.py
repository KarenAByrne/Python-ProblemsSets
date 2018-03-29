#Karen Byrne 29/03/2018
#Exercise 6 Factorial

def factorial(input):
    tempfactx=1                 #need to multiply input by 1 to start the loop
    while input>0:              # while loop down to 1 as per factorial calculation
        tempfactx = tempfactx * (input) # first number is 1*5
        input=input-1           # reduce input by 1 each loop and multiply by previous tempfactx
    return tempfactx            # output next factorial in series to feed back into the loop
    
print("The factorial of 5 is",factorial(5))
print("The factorial of 7 is",factorial(7))
print("The factorial of 10 is",factorial(10))
