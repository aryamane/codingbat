def in1to10(n, outside_mode):
  if n >= 1 and n<=10 and not outside_mode:
    return True
  
  if outside_mode and (n<=1 or n>=10):
    return True
  
  else:
    return False
  
print(in1to10(5, False) )
print(in1to10(11, False))
print(in1to10(11, True) )