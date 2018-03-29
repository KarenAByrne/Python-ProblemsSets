#Karen Byrne 29/03/2018
#Week 5 Iris data recall in neat format

with open("data/iris.csv") as f:
    for line in f:
        print(line.split(',')[:4]) # From discussion post https://learnonline.gmit.ie/mod/forum/discuss.php?d=14986

