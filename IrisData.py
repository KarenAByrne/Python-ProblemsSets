#Karen Byrne 29/03/2018
#Week 5 Iris data recall in neat format

with open("data/iris.csv") as f:
    for line in f:
        print(line.split(',')[0])

