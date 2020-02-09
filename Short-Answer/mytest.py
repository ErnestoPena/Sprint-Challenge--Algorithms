

def counting(n):
  sum = 0
  for i in range(n):
    j = 1
    i = i + 1
    while j < n:
      j *= 2
      sum += 1
  print("For Loops total", i)  
  print("While Loops total", sum)  


#counting(6)


def bunnyEars(bunnies):
  if bunnies == 0:
    return 0

  return 2 + bunnyEars(bunnies-1)

bunnyEars(3)  