#Karen Byrne 29/03/2018
#Week 5 Iris data recall in neat format
# https://learnonline.gmit.ie/mod/forum/discuss.php?d=14986

with open("data/iris.csv") as f:
    for line in f:
       line = line.replace(',',' ') #Replaces commas from the line with a space
       print(line[:11],line[12:16].strip()) #Prints the first 12 (0-11)  characters with a 
       #space instead of a comma, strips 16 characters from the 12th char onwards
