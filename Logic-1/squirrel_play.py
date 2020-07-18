def squirrel_play(temp, is_summer):
  if temp >= 60 and temp<=90 and not is_summer:
    return True
  
  if is_summer and temp>=60 and temp<=100:
    return True
  
  else:
    return False


print(squirrel_play(70, False) )
print(squirrel_play(95, False) )
print(squirrel_play(95, True) )