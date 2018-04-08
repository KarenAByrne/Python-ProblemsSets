# Karen Byrne 18-02-2018
# Week 3 Exercise
# 22-02-2018

i = 17


while (i > 1):        # loop down to 1
    if (i%2 == 0):    # if the number is even
        i = i / 2       # divide by 2 if even
    else:       #number is odd
        i = 3 * i + 1 # multiply by 3 and add 1 if odd
    print(int(i)) # return an integer for i, prints each number and stops when reaches 1
   
