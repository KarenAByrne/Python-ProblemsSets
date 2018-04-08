# Karen Byrne 8th April 2018
# Euler 
# Resources used http://mirimad.com/project-euler-problem-5-solution-python/
# I did a lot of reading around and looking at code but wanted something simple
# to represent my understanding of the problem even if it was not the most 
# elegant or efficient way to do it. I found an answer that suited me at the above
# URL and then adapted it slightly. See previous commits for my own amatuer attempts.
# In order to cut down running time I started at 2520 which was outlined in the 
# question and incremented in 20s as it had to be divisible by 20 so last digit had 
# be zero and second last digit had to be even.  

# define a function to loop through the divisors from 1-20
def ifDividesAll(lcm):
  for i in range(2,21):
      # returns the numner 1-20 (1st numner is 0)
    if lcm % i != 0:
        # when lcm divied by number in range is not evenly divisible
      return False
  return True

lcm = 2520
#Start at the number provided in the question as it cannot be smaller than this
while True:
  if ifDividesAll(lcm):
    break
    # when all divisors from 1-20 return True break and print the final lcm
  else:
    lcm += 20
    # while false increment the lcm in 20's
print(lcm)
# prints the final number when all divisors from 1-20 return no remainder
