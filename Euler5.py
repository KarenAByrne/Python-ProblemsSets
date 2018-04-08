#Karen Byrne 8th April 2018
#Euler 5

SPI = 2520
# Define Smallest positive integer
for i in range(1,20):
        if SPI % i == 0:
            SPI = True
        else:
            SPI = SPI + 2
return SPI

