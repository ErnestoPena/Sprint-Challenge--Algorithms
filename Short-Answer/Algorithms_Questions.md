# Analysis of Algorithms

## Exercise I

Give an analysis of the running time of each snippet of
pseudocode with respect to the input size n of each of the following:

```python
a)  a = 0
    while (a < n * n * n):      # This will increase as n increases by n to the 3
      a = a + n * n             # This will increase as n increases by n to the 2

# for n = 3
#First Round with 3
# a= 0
# a < 27
# a = 0 + 9 = 9
# Second Round with 3
# a = 9 < 27
# a = 9 + 9 = 18
# Third Round with 3
# 18 < 27
# a = 18 + 9 = 27
# Total Rounds = 3
# 
# Testing n = 4
#First Round with 4
# a = 0
# 0 < 64
# a = 0 + 16 = 16
# Second Round with 4
# 16 < 64
# a = 16 + 16 = 32
# Third Round with 4
# 32 < 64
# a = 32 + 16 = 48
# Fourth Round with 4
# 48 < 64
# a 48 + 16 = 64          
# Total Rounds = 4
# Complexity = O(n)
```


```
b)  sum = 0
    for i in range(n):
      j = 1
      while j < n:
        j *= 2
        sum += 1

# Testing and Removing "sum" variable 
# For n = 3
# First Round of for loop
# i = 0 
#    while 1 < 3
#    j = 1 * 2 = 2

#    while 2 < 3
#    j = 2 * 2 = 4
     
# Second Round of for loop
# i = 1
#    while 1 < 3
#    j = 1 * 2 = 2

#    while 2 < 3
#    j = 2 * 2 = 4

# Third Round of for loop
# i = 2
#    while 1 < 3
#    j = 1 * 2 = 2

#    while 2 < 3
#    j = 2 * 2 = 4


#Third Round 
# i = 2
# 
 


```

```
c)  def bunnyEars(bunnies):
      if bunnies == 0:
        return 0

      return 2 + bunnyEars(bunnies-1)
```

## Exercise II

Suppose that you have an n-story building and plenty of eggs. Suppose also that an egg gets broken if it is thrown off floor f or higher, and doesn't get broken if dropped off a floor less than floor f. Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized.

Write out your proposed algorithm in plain English or pseudocode AND give the runtime complexity of your solution.
