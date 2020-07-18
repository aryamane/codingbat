def make_chocolate(small, big, goal):
    
  if goal > (small + (big*5)):
    return -1

  if goal - (big*5) >=0 :
    return goal - (big*5)

  
  if goal % 5 > small:
    return -1
    
  else:
    return goal % 5

print(make_chocolate(4, 1, 9) )
print(make_chocolate(4, 1, 10) )
print(make_chocolate(4, 1, 7) )