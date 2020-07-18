def caught_speeding(speed, is_birthday):
  if is_birthday:
    inc=5
  else:
    inc = 0
  
  if speed<=60+inc:
    return 0
  
  if speed>60+inc and speed<= 80+inc:
    return 1
  
  else:
    return 2

print(caught_speeding(60, False) )
print(caught_speeding(65, False) )
print(caught_speeding(65, True) )