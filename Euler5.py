#Karen Byrne 8th April 2018
#Euler 5)
Smallestpositiveinteger = 2520
#Start at the number provided in the question as it cannot be smaller than this
isdivisible  = True
# Define Smallest positive integer
for i in range(20):
        if Smallestpositiveinteger % (i+1) != 0:
            isdivisible = False
        else:
            Smallestpositiveinteger = Smallestpositiveinteger + 2
print(Smallestpositiveinteger)
