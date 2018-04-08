#Karen Byrne 8th April 2018
#Euler 5)
Num = 2520
SPI = True
# Define Smallest positive integer
for i in range(11,20):
        if Num % i == 0:
            SPI = True
        else:
            Num = Num + 2
print(Num)
