def make_bricks(small, big, goal):
  if goal > (big*5) + small :
    return False
  if small < goal %5:
    return False
  else:
    return True



print(make_bricks(3, 1, 8) )
print(make_bricks(3, 1, 9) )
print(make_bricks(3, 2, 10))